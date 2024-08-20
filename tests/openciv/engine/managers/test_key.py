from __future__ import annotations
import pytest
from openciv.engine.managers.key import KeyManager, Keyable
from openciv.engine.exceptions.key_exception import KeyNotFoundException
from typing import Type, Any


@pytest.fixture
def key_manager() -> KeyManager:
    return KeyManager.get_instance()


@pytest.fixture
def keyable() -> Keyable:
    return Keyable()


@pytest.fixture
def keyable_object() -> Type[Any]:  # noqa: F821
    class KeyableObject(Keyable):
        def __init__(self):
            super().__init__()

    return KeyableObject


@pytest.fixture
def object_with_key() -> Type[Any]:  # noqa: F821
    class ObjectWithKey:
        def __init__(self):
            self._key = None

    return ObjectWithKey


def test_keyable_initial_key_none(keyable: Keyable) -> None:
    assert keyable._key is None  # type: ignore | This is a test, so we don't care about the type or protected access.


def test_set_key(keyable: Keyable) -> None:
    test_key = "test_key"
    keyable.set_key(key=test_key)
    assert keyable._key == test_key  # type: ignore | This is a test, so we don't care about the type or protected access.


def test_register_key(key_manager: KeyManager, keyable: Keyable) -> None:
    key: str = keyable._register_key()  # type: ignore | This is a test, so we don't care about the type or protected access.
    assert keyable._key is not None  # type: ignore | This is a test, so we don't care about the type or protected access.
    assert key_manager.get(key=key) is keyable


def test_unregister_key(key_manager: KeyManager, keyable: Keyable) -> None:
    key: str = keyable._register_key()  # type: ignore | This is a test, so we don't care about the type or protected access.
    keyable._unregister_key()  # type: ignore | This is a test, so we don't care about the type or protected access.
    with pytest.raises(expected_exception=KeyNotFoundException):
        key_manager.get(key)


def test_key_manager_register(key_manager: KeyManager, keyable: Keyable) -> None:
    key: str = key_manager.register(object_to_register=keyable)
    assert key_manager.get(key=key) is keyable


def test_key_manager_generate_key(key_manager: KeyManager) -> None:
    key: str = key_manager._generate_key()  # type: ignore | This is a test, so we don't care about the type or protected access.
    assert isinstance(key, str)


def test_key_manager_delete_with_key(key_manager: KeyManager, keyable: Keyable) -> None:
    key: str = key_manager.register(object_to_register=keyable)
    key_manager.delete(key=key)
    with pytest.raises(expected_exception=KeyNotFoundException):
        key_manager.get(key=key)


def test_key_manager_delete_with_keyable(key_manager: KeyManager, keyable: Keyable) -> None:
    key: str = key_manager.register(object_to_register=keyable)
    key_manager.delete(key=keyable)
    with pytest.raises(expected_exception=KeyNotFoundException):
        key_manager.get(key=key)


def test_key_manager_set(key_manager: KeyManager, keyable: Keyable) -> None:
    key: str = key_manager.register(object_to_register=keyable)
    key_manager.set(key=key, value=keyable)
    assert key_manager.get(key=key) is keyable


def test_key_manager_delete_invalid_type(key_manager: KeyManager, keyable_object: type[Any]) -> None:
    with pytest.raises(expected_exception=KeyNotFoundException):
        key_manager.delete(key=keyable_object())


def test_key_manager_delete_with_invalid_type(key_manager: KeyManager) -> None:
    with pytest.raises(ValueError):
        key_manager.delete(object())


def test_key_manager_register_with_generic_object(key_manager: KeyManager, object_with_key: type[Any]) -> None:
    obj = object_with_key()
    key: str = key_manager.register(object_to_register=obj)
    assert key_manager.get(key=key) is obj


def test_key_manager_register_invalid_type(key_manager: KeyManager) -> None:
    key_manager.register(object_to_register=object())  # type: ignore | This is a test, so we don't care about the type or protected access.
