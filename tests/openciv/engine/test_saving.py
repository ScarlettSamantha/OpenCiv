from openciv.engine.saving import SaveAble
from openciv.engine.exceptions.save_exception import SaveRestorationRestoreTypeInvalidException
from typing import List, Any, Dict
from openciv.engine.managers.i18n import t_

import pytest


# Define a concrete class for testing
class ConcreteSaveAble(SaveAble):
    def __init__(self, prop1: Any, prop2: Any, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self.prop1: Any = prop1
        self.prop2: Any = prop2
        self._setup_saveable()

    def _register_saveable_properties(self) -> List[str]:
        return ["prop1", "prop2"]

    def _register_instance_args(self) -> List[str]:
        return ["prop1", "prop2"]


# Define a concrete class for testing
class ConcreteNestableSaveAble(SaveAble):
    def __init__(self, prop1: Any, prop2: Any, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self.prop1: ConcreteNestableSaveAble = prop1
        self.prop2 = prop2
        self._setup_saveable()

    def _register_saveable_properties(self) -> List[str]:
        return super()._register_saveable_properties()

    def _register_instance_args(self) -> List[str]:
        return super()._register_instance_args()


def test_saveable_data() -> None:
    obj = ConcreteSaveAble(prop1="value1", prop2=42)
    data: Dict[str, Any] = obj.saveable_data()
    assert data["prop1"] == "value1"
    assert data["prop2"] == 42


def test_is_valid_saveable_type() -> None:
    assert SaveAble._is_valid_saveable_type(value="string")  # type: ignore
    assert SaveAble._is_valid_saveable_type(value=123)  # type: ignore
    assert SaveAble._is_valid_saveable_type(value=123.456)  # type: ignore
    assert SaveAble._is_valid_saveable_type(value=True)  # type: ignore
    assert SaveAble._is_valid_saveable_type(value=None)  # type: ignore
    assert SaveAble._is_valid_saveable_type(value=[1, 2, 3])  # type: ignore
    assert SaveAble._is_valid_saveable_type(value=(1, 2, 3))  # type: ignore
    assert SaveAble._is_valid_saveable_type(value={"key": "value"})  # type: ignore
    assert not SaveAble._is_valid_saveable_type(value=object())  # type: ignore


def test_invalid_restore_property() -> None:
    obj = ConcreteSaveAble(prop1=None, prop2=None)
    with pytest.raises(expected_exception=TypeError):
        obj._restore_property(key="prop1", value=object())  # type: ignore


def test_recursive_save_restore() -> None:
    nested_obj = ConcreteNestableSaveAble(prop1="nested_value", prop2=99)  # type: ignore
    obj = ConcreteNestableSaveAble(prop1=nested_obj, prop2=42)
    data: Dict[str, Any] = obj.saveable_data()
    assert data["prop1"]["prop1"] == "nested_value"
    assert data["prop1"]["prop2"] == 99
    assert data["prop2"] == 42

    restored_nested_obj = ConcreteNestableSaveAble(prop1=None, prop2=None)  # type: ignore
    restored_nested_obj.restore_from_data(data=data["prop1"])

    restored_obj = ConcreteNestableSaveAble(prop1=restored_nested_obj, prop2=None)
    restored_obj.restore_from_data(data=data)

    assert isinstance(restored_obj.prop1, ConcreteNestableSaveAble)
    assert restored_obj.prop1.prop1 == "nested_value"
    assert restored_obj.prop1.prop2 == 99
    assert restored_obj.prop2 == 42


def test_register_saveable_properties() -> None:
    obj = ConcreteSaveAble(prop1="value1", prop2=42)
    properties: List[str] = obj._register_saveable_properties()  # type: ignore
    assert properties == ["prop1", "prop2"]

    nested_obj = ConcreteNestableSaveAble(prop1="nested_value", prop2=99)  # type: ignore
    properties = nested_obj._register_saveable_properties()  # type: ignore
    assert properties == ["prop1", "prop2"]


def test_register_instance_args() -> None:
    obj = ConcreteSaveAble(prop1="value1", prop2=42)
    args = obj._register_instance_args()  # type: ignore
    assert args == ["prop1", "prop2"]

    nested_obj = ConcreteNestableSaveAble(prop1="nested_value", prop2=99)
    args: List[str] = nested_obj._register_instance_args()  # type: ignore
    assert args == ["prop1", "prop2"]


def test_eq_method() -> None:
    import uuid

    matching_uuid = str(object=uuid.uuid4())
    obj1 = ConcreteSaveAble(prop1="value1", prop2=42, _key=matching_uuid)
    obj2 = ConcreteSaveAble(prop1="value1", prop2=42, _key=matching_uuid)
    obj3 = ConcreteSaveAble(prop1="value2", prop2=43, _key=str(uuid.uuid4()))

    assert obj1 == obj2
    assert obj1 != obj3

    nested_obj1 = ConcreteNestableSaveAble(prop1="nested_value1", prop2=99, _key=matching_uuid)
    nested_obj2 = ConcreteNestableSaveAble(prop1="nested_value1", prop2=99, _key=matching_uuid)
    nested_obj3 = ConcreteNestableSaveAble(prop1="nested_value2", prop2=100, _key=str(uuid.uuid4()))

    assert nested_obj1 == nested_obj2
    assert nested_obj1 != nested_obj3


def test_module_not_found():
    instance = ConcreteNestableSaveAble(prop1=None, prop2=None)
    data: Dict[str, Any] = {"__type": "non_existent_module.NonExistentClass", "__instance_args": []}
    with pytest.raises(SaveRestorationRestoreTypeInvalidException) as excinfo:
        instance._create_object(data)  # type: ignore
    assert "Module not found" in str(excinfo.value)


def test_class_not_found() -> None:
    instance = ConcreteNestableSaveAble(prop1=None, prop2=None)
    data: Dict[str, Any] = {"__type": "unittest.NonExistentClass", "__instance_args": []}
    with pytest.raises(expected_exception=SaveRestorationRestoreTypeInvalidException) as excinfo:
        instance._create_object(data=data)  # type: ignore
    assert "Class not found" in str(excinfo.value)


def test_object_not_saveable() -> None:
    instance = ConcreteNestableSaveAble(prop1=None, prop2=None)  # type: ignore
    data: Dict[str, Any] = {"__type": "unittest.TestCase", "__instance_args": []}
    with pytest.raises(expected_exception=SaveRestorationRestoreTypeInvalidException) as excinfo:
        instance._create_object(data=data)  # type: ignore
    assert "Object is not a SaveAble" in str(excinfo.value)


####
#
# Tests if implementations of SaveAble are able to be saved and restored.
#
####


def test_improvement_saveable():
    from openciv.gameplay.improvement import Improvement

    improvement = Improvement(key="test.improvement.key", name="test_improvement")
    data: Dict[str, Any] = improvement.saveable_data()
    restored_improvement = Improvement(key="testkey", name="testname")
    restored_improvement.restore_from_data(data=data)

    assert restored_improvement.name == "test_improvement"
    assert restored_improvement.get_state_hash() == improvement.get_state_hash()


def test_saving_civic():
    from openciv.gameplay.culture import Civic
    from openciv.engine.managers.i18n import t_

    civic = Civic(key="test.civic.key", name=t_("test_civic"), description=t_("test_civic_description"))
    data = civic.saveable_data()  # type: ignore

    restored_civic: SaveAble | Civic = Civic.create_object_from_data(data=data)  # type: ignore

    assert restored_civic.name == t_("test_civic")  # type: ignore
    assert restored_civic.description == t_("test_civic_description")  # type: ignore
    assert restored_civic.get_state_hash() == civic.get_state_hash()


def test_saving_great() -> None:
    from openciv.gameplay.great import Great

    class GreatTest(Great):
        def __init__(self) -> None:
            super().__init__(key="test.great.key", name=t_("test_great"), description=t_("test_great_description"))  # type: ignore

    great = GreatTest()
    data: Dict[str, Any] = great.saveable_data()
    restored_great: SaveAble = great.create_object_from_data(data=data)
    assert restored_great.get_state_hash() == great.get_state_hash()


if __name__ == "__main__":
    test_saveable_data()
    test_is_valid_saveable_type()
    test_invalid_restore_property()
    test_recursive_save_restore()
    test_register_saveable_properties()
    test_register_instance_args()
    test_eq_method()
    test_module_not_found()
    test_class_not_found()
    test_object_not_saveable()
    test_improvement_saveable()
    test_saving_civic()
    test_saving_great()
