from openciv.engine.managers.base import BaseManager
from openciv.engine.mixins.singleton import Singleton
from openciv.engine.exceptions.key_exception import KeyNotFoundException
from uuid import uuid4
from typing import Dict


class Keyable:
    """
    Provides a mechanism for assigning and managing unique keys to objects.
    Interacts with KeyManager to ensure each object has a unique identifier.
    """

    def __init__(self, _key: str = None):
        """Initializes a Keyable object with no key assigned initially."""
        self._key: str = _key

    def set_key(self, key: str) -> None:
        """
        Sets the unique key for this object.

        Args:
            key (str): The unique key to be assigned to this object.
        """
        self._key = key

    def _register_key(self) -> str:
        """
        Registers the object with the KeyManager and assigns it a unique key.

        Returns:
            str: The unique key assigned to this object.
        """
        return KeyManager._get_instance().register(self)

    def _unregister_key(self) -> None:
        """
        Unregisters the object's key from the KeyManager.
        """
        KeyManager._get_instance().delete(self._key)


class KeyManager(BaseManager, Singleton):
    """
    Manages unique keys for objects, ensuring each registered object has a unique identifier.
    Implements Singleton pattern to ensure only one instance exists.
    """

    def __setup__(self) -> None:
        """Sets up the key manager by initializing the dictionary to store registered keys."""
        self._registered_keys: Dict[str, object | Keyable] = {}

    def get(self, key: str) -> object:
        """
        Retrieves the object associated with the given key.

        Args:
            key (str): The key of the object to retrieve.

        Returns:
            object: The object associated with the given key.

        Raises:
            KeyNotFoundException: If the key is not found.
        """
        if key not in self._registered_keys:
            raise KeyNotFoundException(f"Key {key} not found.")
        return self._registered_keys[key]

    def set(self, key: str, value: object | Keyable) -> None:
        """
        Associates the given key with the given object.

        Args:
            key (str): The key to associate with the object.
            value (object | Keyable): The object to be associated with the key.
        """
        self._registered_keys[key] = value

    def _generate_key(self) -> str:
        """
        Generates a new unique key.

        Returns:
            str: A new unique key.
        """
        return str(uuid4())

    def delete(self, key: str | object | Keyable) -> None:
        """
        Deletes the key from the manager.

        Args:
            key (str | object | Keyable): The key or object whose key needs to be deleted.

        Raises:
            KeyNotFoundException: If the key is not found.
            ValueError: If the input is not a key or Keyable object.
        """
        if isinstance(key, Keyable):
            key = key._key
        elif not isinstance(key, str):
            raise ValueError("KeyManager.delete() only accepts a key or Keyable object.")
        if key not in self._registered_keys:
            raise KeyNotFoundException(f"Key {key} not found.")
        del self._registered_keys[key]

    def register(self, object_to_register: object) -> str:
        """
        Registers an object with the manager, assigning it a unique key if it doesn't already have one.

        Args:
            object_to_register (object): The object to register.

        Returns:
            str: The unique key assigned to the registered object.

        Raises:
            ValueError: If the object is not Keyable or doesn't have a _key attribute.
        """
        if hasattr(object_to_register, "_key") and object_to_register._key is not None:
            key = object_to_register._key
        else:
            key = self._generate_key()
            if isinstance(object_to_register, Keyable):
                object_to_register.set_key(key)
            elif hasattr(object_to_register, "_key"):
                object_to_register._key = key
            else:
                raise ValueError("KeyManager.register() only accepts a Keyable object with a _key attribute.")

        self._registered_keys[key] = object_to_register
        return key
