from openciv.engine.managers.key import Keyable
from datetime import datetime
from openciv.engine.exceptions.save_exception import (
    SaveRestorationRestoreTypeInvalidException,
    SaveRestoreObjectNotRestorableException,
)
import abc
from typing import Dict, List, TypeVar, Any, ForwardRef

# Define a type variable for saveable properties with self-reference
SaveableType = TypeVar(
    "SaveableType", str, int, float, bool, List[ForwardRef("SaveableType")], Dict[str, ForwardRef("SaveableType")], None
)


class SaveAble(Keyable):
    """
    SaveAble is an abstract base class designed to facilitate the saving and restoring
    of arbitrary objects. This class provides a structured way to define
    properties that can be serialized (saved) and deserialized (restored). The goal
    is to enable game objects to persist their state across sessions, making it easier
    to implement save/load functionality.
    """

    def __init__(self, *args: Any, **kwargs: Any):
        """Initialize SaveAble object, register key, and saveable properties."""
        super().__init__(*args, **kwargs)
        self._register_key()
        self._meta_properties: List[str] = [
            "__type",
            "_saveable_properties",
            "_instance_args",
            "_use_auto_save",
            "_restorable",
            "_restored_on",
        ]
        self._saveable_properties: List[str] = self._register_saveable_properties()
        self._saveable_properties.append("_key")  # Add _key property to saveable properties
        self._instance_args: List[str] = self._register_instance_args()
        self._use_auto_save: bool = True
        self._restorable: bool = True

        self._restored_on: bool | datetime = False

    @abc.abstractmethod
    def _register_instance_args(self) -> List[str]:
        """Abstract method to register instance arguments.
        Must be implemented by child classes.

        Returns:
            List[str]: List of instance arguments.
        """
        pass

    @abc.abstractmethod
    def _register_saveable_properties(self) -> List[str]:
        """Abstract method to register saveable properties.
        Must be implemented by child classes.

        Returns:
            List[str]: List of saveable properties.
        """
        pass

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
        setattr(self, key, value)

    def _save_property(self, key: str, auto_recursion: bool = True) -> SaveableType:
        """Save a property to a saveable format.
        Can be overridden in child classes for custom processing.

        Args:
            key (str): The key of the property to save.
            auto_recursion (bool): Whether to automatically save subobjects.

        Returns:
            SaveableType: The saved property value.
        """
        value = getattr(self, key)
        if isinstance(value, SaveAble) and auto_recursion:
            return value.saveable_data()
        return value

    def restore_object(self, data: Dict[str, SaveableType]) -> None:
        """Restore the object from saved data.

        Args:
            data (Dict[str, SaveableType]): The saved data.
        """
        if not self._restorable:
            raise SaveRestoreObjectNotRestorableException(f"Object is not restorable: {self}")
        self.restore_from_data(data)

    def saveable_data(self) -> Dict[str, SaveableType]:
        """Get the saveable data of the object.

        Returns:
            Dict[str, SaveableType]: The saveable data.
        """
        data = {
            "__type": f"{self.__module__}.{self.__class__.__name__}",
            "__instance_args": self._instance_args,
        }
        for key in self._saveable_properties:
            data[key] = self._save_property(key)
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

    def _create_object(self, data: Dict[str, SaveableType]) -> "SaveAble":
        """Create an object from saved data.

        Args:
            data (Dict[str, SaveableType]): The saved data.

        Returns:
            SaveAble: The created object.
        """
        module_name, class_name = data["__type"].rsplit(".", 1)
        _kwargs = (
            {}
            if "__instance_args" not in data or data["__instance_args"] is None
            else {k: v for k, v in data.items() if k in data["__instance_args"]}
        )
        try:
            module = __import__(module_name, fromlist=[class_name])
        except ModuleNotFoundError:
            raise SaveRestorationRestoreTypeInvalidException(
                f"Module not found: {module_name}. Please ensure that the module is importable. This could be a mod not being loaded."
            )
        try:
            class_ = getattr(module, class_name)
        except AttributeError:
            raise SaveRestorationRestoreTypeInvalidException(
                f"Class not found: {class_name} in module {module_name}. Please ensure that the class is defined in the module. This could be a mod not being loaded."
            )
        obj = class_(**_kwargs)
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
        valid_types = (str, int, float, bool, type(None), SaveAble)
        if isinstance(value, valid_types):
            return True
        if isinstance(value, type) and issubclass(value, valid_types):
            return True
        if isinstance(value, list):
            return all(SaveAble._is_valid_saveable_type(item) for item in value)
        if isinstance(value, dict):
            return all(isinstance(k, str) and SaveAble._is_valid_saveable_type(v) for k, v in value.items())
        return False

    def __eq__(self, other):
        if isinstance(other, SaveAble):
            return self._key == other._key
        else:
            return False
