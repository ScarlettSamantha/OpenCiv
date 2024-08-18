from __future__ import annotations
import pytest
from openciv.engine.managers.key import KeyManager, Keyable
from openciv.engine.exceptions.key_exception import KeyNotFoundException


@pytest.fixture
def key_manager():
    return KeyManager.get_instance()


@pytest.fixture
def keyable():
    return Keyable()


@pytest.fixture
def keyable_object():
    class KeyableObject(Keyable):
        def __init__(self):
            super().__init__()

    return KeyableObject


@pytest.fixture
def object_with_key():
    class ObjectWithKey:
        def __init__(self):
            self._key = None

    return ObjectWithKey


def test_keyable_initial_key_none(keyable):
    assert keyable._key is None


def test_set_key(keyable):
    test_key = "test_key"
    keyable.set_key(test_key)
    assert keyable._key == test_key


def test_register_key(key_manager, keyable):
    key = keyable._register_key()
    assert keyable._key is not None
    assert key_manager.get(key) is keyable


def test_unregister_key(key_manager, keyable):
    key = keyable._register_key()
    keyable._unregister_key()
    with pytest.raises(KeyNotFoundException):
        key_manager.get(key)


def test_key_manager_register(key_manager, keyable):
    key = key_manager.register(keyable)
    assert key_manager.get(key) is keyable


def test_key_manager_generate_key(key_manager):
    key = key_manager._generate_key()
    assert isinstance(key, str)


def test_key_manager_delete_with_key(key_manager, keyable):
    key = key_manager.register(keyable)
    key_manager.delete(key)
    with pytest.raises(KeyNotFoundException):
        key_manager.get(key)


def test_key_manager_delete_with_keyable(key_manager, keyable):
    key = key_manager.register(keyable)
    key_manager.delete(keyable)
    with pytest.raises(KeyNotFoundException):
        key_manager.get(key)


def test_key_manager_set(key_manager, keyable):
    key = key_manager.register(keyable)
    key_manager.set(key, keyable)
    assert key_manager.get(key) is keyable


def test_key_manager_delete_invalid_type(key_manager, keyable_object):
    with pytest.raises(KeyNotFoundException):
        key_manager.delete(keyable_object())


def test_key_manager_delete_with_invalid_type(key_manager):
    with pytest.raises(ValueError):
        key_manager.delete(object())


def test_key_manager_register_with_generic_object(key_manager, object_with_key):
    obj = object_with_key()
    key = key_manager.register(obj)
    assert key_manager.get(key) is obj


def test_key_manager_register_invalid_type(key_manager):
    with pytest.raises(ValueError):
        key_manager.register(object())
