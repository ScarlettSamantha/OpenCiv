import pytest
from openciv.engine.exceptions.condition_exception import ConditionObjectPropertyDoesNotExist
from openciv.engine.requires import Condition, ConditionMultiple, Requires, RequiresMultiple


class PropertyObject:
    def __init__(self, test_property=None):
        self.test_property = test_property


@pytest.fixture
def _PropertyObject(*args, **kwargs) -> PropertyObject:
    return PropertyObject(*args, **kwargs)


def test_checkCondition_property_exists(_PropertyObject: PropertyObject):
    _PropertyObject.test_property = "value"
    condition = Condition(_PropertyObject, "test_property", "value")

    assert condition.checkCondition() is True


def test_checkCondition_property_does_not_exist(_PropertyObject: PropertyObject):
    condition = Condition(_PropertyObject, "non_existent_property", "value")

    with pytest.raises(ConditionObjectPropertyDoesNotExist):
        condition.checkCondition()


def test_checkCondition_property_function(_PropertyObject: PropertyObject):
    _PropertyObject.test_property = lambda: "value"
    condition = Condition(_PropertyObject, "test_property", "value")

    assert condition.checkCondition() is True


def test_repr(_PropertyObject: PropertyObject):
    _PropertyObject.test_property = "value"
    condition = Condition(_PropertyObject, "test_property", "value")

    repr_str = f"Condition[obj={_PropertyObject}, property=test_property, required_value=value] -> True"
    assert repr(condition) == repr_str


@pytest.fixture
def condition_true() -> Condition:
    class TrueCondition(Condition):
        def checkCondition(self):
            return True

    return TrueCondition(None, "", "")


@pytest.fixture
def condition_false() -> Condition:
    class FalseCondition(Condition):
        def checkCondition(self):
            return False

    return FalseCondition(None, "", "")


def test_checkCondition_all_true(condition_true: Condition):
    condition_multiple = ConditionMultiple([condition_true, condition_true], None, "property", "value")
    assert condition_multiple.checkCondition() is True


def test_checkCondition_one_false(condition_true: Condition, condition_false: Condition):
    condition_multiple = ConditionMultiple([condition_true, condition_false], None, "property", "value")
    assert condition_multiple.checkCondition() is False


def test_requires_inherits_condition(_PropertyObject: PropertyObject):
    _PropertyObject.test_property = "value"
    requires = Requires(_PropertyObject, "test_property", "value")

    assert isinstance(requires, Condition)
    assert requires.checkCondition() is True


def test_requiresMultiple_inherits_conditionMultiple(condition_true: Condition):
    requires_multiple = RequiresMultiple([condition_true, condition_true], None, "property", "value")
    assert isinstance(requires_multiple, ConditionMultiple)
    assert requires_multiple.checkCondition() is True
