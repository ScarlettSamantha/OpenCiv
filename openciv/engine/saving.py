from openciv.engine.managers.key import Keyable
from openciv.engine.managers.log import LogManager
from openciv.engine.mixins.statehash import StateHashable
from datetime import datetime
from openciv.engine.exceptions.save_exception import (
    SaveRestoreObjectPropertyObjectInvalidRestoreStateException,
    SaveRestorationRestoreTypeInvalidException,
    SaveRestoreObjectNotRestorableException,
    SavePropertyIsObjectButNotSaveAbleException,
)
import inspect
from abc import ABCMeta
from logging import DEBUG
from typing import Dict, List, TypeVar, Any, ForwardRef, Tuple, Callable

# Define a type variable for saveable properties with self-reference
SaveableType = TypeVar(
    "SaveableType", str, int, float, bool, List[ForwardRef("SaveableType")], Dict[str, ForwardRef("SaveableType")], None
)

# This is to enable debug timers if the log level is set to DEBUG
if LogManager._get_instance().engine.getEffectiveLevel() <= DEBUG:
    _debug_timers: Dict[str, datetime] = {}
    _debug_timer_enable: bool = True
else:
    _debug_timer_enable: bool = False


def md5_hash(value: Any) -> str:
    import hashlib

    PREFIX = "md5:"
    return f"{PREFIX}{hashlib.md5(str(value).encode()).hexdigest()}"


signature_map: Dict[str, Callable] = {
    "md5": md5_hash,
}


def hash_saveable_type(value: SaveableType, hash_func: Callable[[Any], int] = md5_hash) -> str:
    """
    Hashes a SaveableType object, recursively handling lists and dictionaries.

    :param value: The value to hash.
    :param hash_func: The hashing function to use.
    :return: The hash of the value.
    """
    if isinstance(value, (str, int, float, bool, type(None))):
        return hash_func(value)
    elif isinstance(value, list):
        return hash_func(tuple(hash_saveable_type(v, hash_func) for v in value))
    elif isinstance(value, dict):
        return hash_func(frozenset((k, hash_saveable_type(v, hash_func)) for k, v in value.items()))
    elif isinstance(value, SaveAble):
        return value.get_state_hash()
    else:
        raise TypeError(f"Unsupported type for hashing: {type(value)}")


def nosave(f):
    """
    Decorator to mark properties that should not be saved.
    """
    f._nosave = True
    return f


class SaveAble(Keyable, StateHashable):
    """
    SaveAble is an abstract base class designed to facilitate the saving and restoring
    of arbitrary objects. This class provides a structured way to define
    properties that can be serialized (saved) and deserialized (restored). The goal
    is to enable game objects to persist their state across sessions, making it easier
    to implement save/load functionality.
    """

    def __init__(self, *args: Any, **kwargs: Any):
        """Initialize SaveAble object, register key, and saveable properties."""
        StateHashable.__init__(self)
        Keyable.__init__(self, *args, **kwargs)
        self._meta_properties: List[str] = [
            "_key",
            "__type",
            "_saveable_properties",
            "_instance_args",
            "_use_auto_save",
            "_restorable",
            "_restored_on",
        ]
        self._disable_auto_property_detection: bool = False
        self._saveable_properties: List[str] = []
        self._add_default_saveable_properties()
        self._instance_args: List[str] = []
        self._use_auto_save: bool = True
        self._restorable: bool = True
        self._restore_failure_reasons: List[str] = []

        self._restored_on: bool | datetime = False
        self._register_key()

    def __call__(self, *args: Any, **kwargs: Any):
        """Call the object."""
        rv = super().__call__(*args, **kwargs)
        if not rv._disable_auto_property_detection:
            rv._register_saveable_properties()
        return rv

    def _add_default_saveable_properties(self) -> None:
        self._saveable_properties.append("_key")  # Add _key property to saveable properties

    def _setup_saveable(self, use_auto_save: bool = True, restorable: bool = True) -> None:
        """Setup the saveable properties.
        This should be called at the bottom of the constructor or when the properties are all defined in the class.
        as this will attempt to parse the class for properties.

        Args:
            use_auto_save (bool): Whether to use auto save.
            restorable (bool): Whether the object is restorable.
        """
        self._saveable_properties: List[str] = self._register_saveable_properties()
        self._add_default_saveable_properties()
        self._instance_args: List[str] = self._register_instance_args()

    def _register_instance_args(self) -> List[str]:
        """
        Registers instance arguments that have corresponding class properties.

        Returns:
            List[str]: List of instance argument names that have corresponding properties.
        """
        instance_args: List = []
        for key, parameter in inspect.signature(self.__init__).parameters.items():
            if hasattr(self, key) and not key.startswith("_"):
                instance_args.append(key)
        return instance_args

    def _register_saveable_properties(self) -> List[str]:
        """
        Registers saveable properties.
        Excludes properties starting with an underscore and those marked with @nosave.

        Returns:
            List[str]: List of saveable properties.
        """
        r = []
        for prop in self.__dict__.keys():
            if not prop.startswith("_") and prop not in self._meta_properties:
                attr = getattr(self, prop)
                if not (callable(attr) and getattr(attr, "_nosave", False)):
                    r.append(prop)
        return r

    def validate_state(self, previous_state_hash: str) -> bool:
        """Validate the object's state.
        Must be implemented by child classes.

        Returns:
            bool: True if the object's state is valid, False otherwise.
        """
        own_state_hash = self.get_state_hash()
        _state_hash_eq = self.remove_hash_tag(own_state_hash) == self.remove_hash_tag(previous_state_hash)
        LogManager._get_instance().engine.debug(
            f"Validating state for {self.__class__.__name__}.{self._key} {own_state_hash} == {previous_state_hash} -> {"MATCH!!" if _state_hash_eq else "!!NO MATCH"}"
        )
        return _state_hash_eq

    def _restore_property(self, key: str, value: SaveableType) -> None:
        """Restore a property from the saved data.
        Can be overridden in child classes for custom processing.

        Args:
            key (str): The key of the property to restore.
            value (SaveableType): The value of the property to restore.
        """
        if not self._is_valid_saveable_type(value):
            raise TypeError(f"Invalid type for property '{key}': {type(value).__name__}")

        if key in self._meta_properties:
            return

        # If the value is a dict with a '__class__' key, it might represent a SaveAble object.
        if isinstance(value, dict) and "__type" in value:
            class_name: str = value.pop("__type")
            # Assuming there's a method to get a class by name
            obj_class: object = self._get_class_by_name(class_name)
            if issubclass(obj_class, SaveAble):
                obj: ForwardRef("SaveAble") = obj_class()
                obj.restore_from_data(value)
                setattr(self, key, obj)
                return

        setattr(self, key, value)

    def _save_property(
        self, key: str, auto_recursion: bool = True, permissive_object_saving: bool = False, _recursion_level: int = 0
    ) -> SaveableType:
        """Save a property to a saveable format.
        Can be overridden in child classes for custom processing.

        Args:
            key (str): The key of the property to save.
            auto_recursion (bool): Whether to automatically save subobjects.
            permissive_object_saving (bool): Whether to allow saving objects that are not SaveAble.

        Returns:
            SaveableType: The saved property value.
        """
        value = getattr(self, key)
        if isinstance(value, SaveAble) and auto_recursion:
            return value.saveable_data(parent_recursion_level=_recursion_level)
        elif isinstance(value, object) and not self._is_valid_saveable_type(value):
            if not permissive_object_saving:
                full_class_path: str = f"{value.__module__}.{value.__class__.__name__}"
                own_full_class_path: str = f"{self.__module__}.{self.__class__.__name__}"
                raise SavePropertyIsObjectButNotSaveAbleException(
                    f"Property is object but not SaveAble property: [{own_full_class_path}.{key}] -> [Unsaveable Type({full_class_path})]"
                )
            else:
                full_class_path: str = f"{value.__module__}.{value.__class__.__name__}"
                LogManager._get_instance().engine.warning(f"Object is not SaveAble: {full_class_path}")
                return value if not hasattr(value, "__str__") else str(value)
        return value

    def restore_object(
        self, data: Dict[str, SaveableType], ignore_object_restore_failure: bool = False, _recursion_counter: int = 0
    ) -> None:
        """Restore the object from saved data.

        Args:
            data (Dict[str, SaveableType]): The saved data.
        """
        global _debug_timer_enable
        if _debug_timer_enable:
            _debug_timers[self._key] = datetime.now()

        if not self._restorable:
            raise SaveRestoreObjectNotRestorableException(f"Object is not restorable: {self}")
        self.restore_from_data(data)
        if self.validate_state(data["__hash"]) is False:
            if ignore_object_restore_failure:
                LogManager._get_instance().engine.warning(
                    f"Object failed to validate state: {self.__class__.__name__}.{self._key}"
                )
                return
            else:
                reasons: str = ", ".join(self._restore_failure_reasons)
                raise SaveRestoreObjectPropertyObjectInvalidRestoreStateException(
                    "Object failed to validate state Reasons given: {reasons}"
                )

        self._restored_on = datetime.now()

        if _debug_timer_enable:
            LogManager._get_instance().engine.debug(
                f"Restoring took: {round((datetime.now() - _debug_timers[self._key]).total_seconds() * 1000, 4)}"
            )
            del _debug_timers[self._key]

    def saveable_data(
        self, parent_recursion_level: int = -1, _calculate_state_hash: bool = True
    ) -> Dict[str, SaveableType]:
        """Get the saveable data of the object.

        Returns:
            Dict[str, SaveableType]: The saveable data.
        """
        recursion_level: int = parent_recursion_level + 1
        global _debug_timer_enable
        if _debug_timer_enable:
            _debug_timers[self._key] = datetime.now()

        if self._key is None:
            self._register_key()

        data = {
            "__type": f"{self.__module__}.{self.__class__.__name__}",
            "__hash": self.get_state_hash() if _calculate_state_hash else None,
            "__instance_args": self._instance_args,
        }
        LogManager._get_instance().engine.debug(
            f"Saving[{self.__class__.__name__}.{self._key}][R_L:{recursion_level}]: {self.__module__}.{self.__class__.__name__}"
        )
        for key in self._saveable_properties:
            data[key] = self._save_property(key, _recursion_level=recursion_level)

        if _debug_timer_enable:
            LogManager._get_instance().engine.debug(
                f"Saving[{self.__class__.__name__}.{self._key}][R_L:{recursion_level}]: took {round((datetime.now() - _debug_timers[self._key]).total_seconds() * 1000, 4)}ms"
            )
            del _debug_timers[self._key]

        return data

    def restore_from_data(self, data: Dict[str, SaveableType]) -> None:
        """Restore the object from saved data.

        Args:
            data (Dict[str, SaveableType]): The saved data.
        """
        for key, value in data.items():
            if isinstance(value, dict) and "__type" in value:
                value = self._create_object(value)
            self._restore_property(key, value)
        self._register_key()
        self._restored_on = datetime.now()
        self.validate_state(data["__hash"])

    @classmethod
    def create_object_from_data(cls, data: Dict[str, SaveableType]) -> ForwardRef("SaveAble"):
        """Create an object from saved data.

        Args:
            data (Dict[str, SaveableType]): The saved data.

        Returns:
            SaveAble: The created object.
        """
        instance_args = data.pop("__instance_args", None)
        instance = cls(**{k: v for k, v in data.items() if k in instance_args})
        instance.restore_from_data({k: v for k, v in data.items() if k != "__instance_args"})
        return instance

    @staticmethod
    def _create_object(data: Dict[str, SaveableType]) -> ForwardRef("SaveAble"):
        """Create an object from saved data.

        Args:
            data (Dict[str, SaveableType]): The saved data.

        Returns:
            SaveAble: The created object.
        """

        module_name, class_name = data["__type"].rsplit(".", 1)
        LogManager._get_instance().engine.debug(f"Creating object from data: {module_name}.{class_name}ms")
        _kwargs = (
            {}
            if "__instance_args" not in data or data["__instance_args"] is None
            else {k: v for k, v in data.items() if k in data["__instance_args"]}
        )
        try:
            module: object = __import__(module_name, fromlist=[class_name])
        except ModuleNotFoundError:
            raise SaveRestorationRestoreTypeInvalidException(
                f"Module not found: {module_name}. Please ensure that the module is importable. This could be a mod not being loaded."
            )
        try:
            class_: str = getattr(module, class_name)
        except AttributeError:
            raise SaveRestorationRestoreTypeInvalidException(
                f"Class not found: {class_name} in module {module_name}. Please ensure that the class is defined in the module. This could be a mod not being loaded."
            )
        obj: object = class_(**_kwargs)
        if not isinstance(obj, SaveAble):
            raise SaveRestorationRestoreTypeInvalidException(
                f"Object is not a SaveAble: {obj} in {module_name}.{class_name}. Please ensure that the object is a subclass of SaveAble. This could be a mod not being loaded."
            )
        obj.restore_from_data(data)
        return obj

    @staticmethod
    def _is_valid_saveable_type(value: Any) -> bool:
        """Check if the value is of a valid saveable type.

        Args:
            value (Any): The value to check.

        Returns:
            bool: True if the value is a valid saveable type, False otherwise.
        """
        valid_types: Tuple = (str, int, float, bool, type(None), SaveAble)
        if isinstance(value, valid_types):
            return True
        if isinstance(value, type) and issubclass(value, valid_types):
            return True
        if isinstance(value, list) or isinstance(value, tuple):
            return all(SaveAble._is_valid_saveable_type(item) for item in value)
        if isinstance(value, dict):
            return all(isinstance(k, str) and SaveAble._is_valid_saveable_type(v) for k, v in value.items())
        return False

    def __eq__(self, other) -> bool:
        if isinstance(other, SaveAble):
            return self._key == other._key
        else:
            return False

    def get_state_hash(self) -> str:
        """Get the state hash of the object.
        Must be implemented by child classes.

        Returns:
            str: The state hash of the object.
        """
        state_hash = ""
        for prop in list(set(self._saveable_properties) - set(self._meta_properties)):
            if hasattr(self, prop):
                partial_hash = hash_saveable_type(getattr(self, prop))
                state_hash += partial_hash
        return hash_saveable_type(state_hash)

    @classmethod
    def remove_hash_tag(cls, hash: str, _get_hash_method: bool = False) -> Tuple[str, str] | str:
        """Get the remote hash tag of the class.

        Returns:
            str: The remote hash tag of the class.
        """
        if hash.find(":") == -1:
            return hash

        split = hash.split(":")
        if _get_hash_method:
            return split[1], split[0]
        else:
            return split[1]
