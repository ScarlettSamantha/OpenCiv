# Define a concrete class for testing
from openciv.engine.saving import SaveAble
from openciv.engine.exceptions.save_exception import SaveRestorationRestoreTypeInvalidException
from typing import ForwardRef, List

import pytest


# Define a concrete class for testing
class ConcreteSaveAble(SaveAble):
    def __init__(self, prop1, prop2, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.prop1 = prop1
        self.prop2 = prop2
        self._setup_saveable()

    def _register_saveable_properties(self) -> List:
        return ["prop1", "prop2"]

    def _register_instance_args(self) -> List:
        return ["prop1", "prop2"]


# Define a concrete class for testing
class ConcreteNestableSaveAble(SaveAble):
    def __init__(self, prop1: ForwardRef("ConcreteNestableSaveAble"), prop2, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.prop1 = prop1
        self.prop2 = prop2
        self._setup_saveable()

    def _register_saveable_properties(self) -> List:
        return super()._register_saveable_properties()

    def _register_instance_args(self) -> List:
        return super()._register_instance_args()


def test_saveable_data():
    obj = ConcreteSaveAble("value1", 42)
    data = obj.saveable_data()
    assert data["prop1"] == "value1"
    assert data["prop2"] == 42


def test_is_valid_saveable_type():
    assert SaveAble._is_valid_saveable_type("string")
    assert SaveAble._is_valid_saveable_type(123)
    assert SaveAble._is_valid_saveable_type(123.456)
    assert SaveAble._is_valid_saveable_type(True)
    assert SaveAble._is_valid_saveable_type(None)
    assert SaveAble._is_valid_saveable_type([1, 2, 3])
    assert SaveAble._is_valid_saveable_type((1, 2, 3))
    assert SaveAble._is_valid_saveable_type({"key": "value"})
    assert not SaveAble._is_valid_saveable_type(object())


def test_invalid_restore_property():
    obj = ConcreteSaveAble(None, None)
    with pytest.raises(TypeError):
        obj._restore_property("prop1", object())


def test_recursive_save_restore():
    nested_obj = ConcreteNestableSaveAble("nested_value", 99)
    obj = ConcreteNestableSaveAble(nested_obj, 42)
    data = obj.saveable_data()
    print(data)
    assert data["prop1"]["prop1"] == "nested_value"
    assert data["prop1"]["prop2"] == 99
    assert data["prop2"] == 42

    restored_nested_obj = ConcreteNestableSaveAble(None, None)
    restored_nested_obj.restore_from_data(data["prop1"])

    restored_obj = ConcreteNestableSaveAble(restored_nested_obj, None)
    restored_obj.restore_from_data(data)

    assert isinstance(restored_obj.prop1, ConcreteNestableSaveAble)
    assert restored_obj.prop1.prop1 == "nested_value"
    assert restored_obj.prop1.prop2 == 99
    assert restored_obj.prop2 == 42


def test_register_saveable_properties():
    obj = ConcreteSaveAble("value1", 42)
    properties = obj._register_saveable_properties()
    assert properties == ["prop1", "prop2"]

    nested_obj = ConcreteNestableSaveAble("nested_value", 99)
    properties = nested_obj._register_saveable_properties()
    assert properties == ["prop1", "prop2"]


def test_register_instance_args():
    obj = ConcreteSaveAble("value1", 42)
    args = obj._register_instance_args()
    assert args == ["prop1", "prop2"]

    nested_obj = ConcreteNestableSaveAble("nested_value", 99)
    args = nested_obj._register_instance_args()
    assert args == ["prop1", "prop2"]


def test_eq_method():
    import uuid

    matching_uuid = str(uuid.uuid4())
    obj1 = ConcreteSaveAble("value1", 42, _key=matching_uuid)
    obj2 = ConcreteSaveAble("value1", 42, _key=matching_uuid)
    obj3 = ConcreteSaveAble("value2", 43, _key=str(uuid.uuid4()))

    assert obj1 == obj2
    assert obj1 != obj3

    nested_obj1 = ConcreteNestableSaveAble("nested_value1", 99, _key=matching_uuid)
    nested_obj2 = ConcreteNestableSaveAble("nested_value1", 99, _key=matching_uuid)
    nested_obj3 = ConcreteNestableSaveAble("nested_value2", 100, _key=str(uuid.uuid4()))

    assert nested_obj1 == nested_obj2
    assert nested_obj1 != nested_obj3


def test_module_not_found():
    instance = ConcreteNestableSaveAble(None, None)
    data = {"__type": "non_existent_module.NonExistentClass", "__instance_args": []}
    with pytest.raises(SaveRestorationRestoreTypeInvalidException) as excinfo:
        instance._create_object(data)
    assert "Module not found" in str(excinfo.value)


def test_class_not_found():
    instance = ConcreteNestableSaveAble(None, None)
    data = {"__type": "unittest.NonExistentClass", "__instance_args": []}
    with pytest.raises(SaveRestorationRestoreTypeInvalidException) as excinfo:
        instance._create_object(data)
    assert "Class not found" in str(excinfo.value)


def test_object_not_saveable():
    instance = ConcreteNestableSaveAble(None, None)
    data = {"__type": "unittest.TestCase", "__instance_args": []}
    with pytest.raises(SaveRestorationRestoreTypeInvalidException) as excinfo:
        instance._create_object(data)
    assert "Object is not a SaveAble" in str(excinfo.value)


####
#
# Tests if implementations of SaveAble are able to be saved and restored.
#
####


def test_improvement_saveable():
    from openciv.gameplay.improvement import Improvement

    improvement = Improvement("test.improvement.key", "test_improvement")
    data = improvement.saveable_data()
    restored_improvement = Improvement(None, None)
    restored_improvement.restore_from_data(data)

    assert restored_improvement.name == "test_improvement"
    assert restored_improvement.effects.collection_name == "test_improvement"
    assert restored_improvement.get_state_hash() == improvement.get_state_hash()
