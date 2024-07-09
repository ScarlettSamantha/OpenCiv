# Define a concrete class for testing
from openciv.engine.saving import SaveAble
from typing import ForwardRef, List

import pytest


# Define a concrete class for testing
class ConcreteSaveAble(SaveAble):
    def __init__(self, prop1, prop2):
        self.prop1 = prop1
        self.prop2 = prop2
        super().__init__()

    def _register_saveable_properties(self) -> List:
        return ["prop1", "prop2"]

    def _register_instance_args(self) -> List:
        return ["prop1", "prop2"]


# Define a concrete class for testing
class ConcreteNestableSaveAble(SaveAble):
    def __init__(self, prop1: ForwardRef("ConcreteNestableSaveAble"), prop2):
        self.prop1 = prop1
        self.prop2 = prop2
        super().__init__()

    def _register_saveable_properties(self) -> List:
        return ["prop1", "prop2"]

    def _register_instance_args(self) -> List:
        return ["prop1", "prop2"]


def test_saveable_data():
    obj = ConcreteSaveAble("value1", 42)
    data = obj.saveable_data()
    assert data["prop1"] == "value1"
    assert data["prop2"] == 42


def test_restore_from_data():
    obj = ConcreteSaveAble(None, None)
    data = {"prop1": "value1", "prop2": 42}
    obj.restore_from_data(data)
    assert obj.prop1 == "value1"
    assert obj.prop2 == 42


def test_is_valid_saveable_type():
    assert SaveAble._is_valid_saveable_type("string")
    assert SaveAble._is_valid_saveable_type(123)
    assert SaveAble._is_valid_saveable_type(123.456)
    assert SaveAble._is_valid_saveable_type(True)
    assert SaveAble._is_valid_saveable_type(None)
    assert SaveAble._is_valid_saveable_type([1, 2, 3])
    assert SaveAble._is_valid_saveable_type({"key": "value"})
    assert not SaveAble._is_valid_saveable_type(object())


def test_invalid_restore_property():
    obj = ConcreteSaveAble(None, None)
    with pytest.raises(TypeError):
        obj._restore_property("prop1", object())


def test_restore_object():
    obj = ConcreteSaveAble(None, None)
    data = {"prop1": "value1", "prop2": 42}
    obj.restore_object(data)
    assert obj.prop1 == "value1"
    assert obj.prop2 == 42


def test_recursive_save_restore():
    nested_obj = ConcreteNestableSaveAble("nested_value", 99)
    obj = ConcreteNestableSaveAble(nested_obj, 42)
    data = obj.saveable_data()

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
