from __future__ import annotations
import pytest
from openciv.engine.exceptions.condition_exception import ConditionObjectPropertyDoesNotExist
from openciv.engine.requires import Condition, ConditionMultiple, Requires, RequiresMultiple
from typing import Any, Literal


class PropertyObject:
    def __init__(self, test_property: Any = None) -> None:
        self.test_property = test_property


@pytest.fixture
def _PropertyObject(*args: Any, **kwargs: Any) -> PropertyObject:  # type: ignore
    return PropertyObject(*args, **kwargs)


def test_checkCondition_property_exists(_PropertyObject: PropertyObject) -> None:
    _PropertyObject.test_property = "value"
    condition = Condition(obj=_PropertyObject, property="test_property", required_value="value")

    assert condition.checkCondition() is True


def test_checkCondition_property_does_not_exist(_PropertyObject: PropertyObject) -> None:
    condition = Condition(obj=_PropertyObject, property="non_existent_property", required_value="value")

    with pytest.raises(expected_exception=ConditionObjectPropertyDoesNotExist):
        condition.checkCondition()


def test_checkCondition_property_function(_PropertyObject: PropertyObject) -> None:
    _PropertyObject.test_property = lambda: "value"
    condition = Condition(obj=_PropertyObject, property="test_property", required_value="value")

    assert condition.checkCondition() is True


def test_repr(_PropertyObject: PropertyObject) -> None:
    _PropertyObject.test_property = "value"
    condition = Condition(obj=_PropertyObject, property="test_property", required_value="value")

    repr_str: str = f"Condition[obj={_PropertyObject}, property=test_property, required_value=value] -> True"
    assert repr(condition) == repr_str


@pytest.fixture
def condition_true() -> Condition:
    class TrueCondition(Condition):
        def checkCondition(self) -> Literal[True]:
            return True

    return TrueCondition(obj=None, property="", required_value="")


@pytest.fixture
def condition_false() -> Condition:
    class FalseCondition(Condition):
        def checkCondition(self) -> Literal[False]:
            return False

    return FalseCondition(obj=None, property="", required_value="")


def test_checkCondition_all_true(condition_true: Condition) -> None:
    condition_multiple = ConditionMultiple([condition_true, condition_true], None, "property", "value")
    assert condition_multiple.checkCondition() is True


def test_checkCondition_one_false(condition_true: Condition, condition_false: Condition) -> None:
    condition_multiple = ConditionMultiple([condition_true, condition_false], None, "property", "value")
    assert condition_multiple.checkCondition() is False


def test_requires_inherits_condition(_PropertyObject: PropertyObject) -> None:
    _PropertyObject.test_property = "value"
    requires = Requires(_PropertyObject, "test_property", "value")

    assert isinstance(requires, Condition)
    assert requires.checkCondition() is True


def test_requiresMultiple_inherits_conditionMultiple(condition_true: Condition) -> None:
    requires_multiple = RequiresMultiple([condition_true, condition_true], None, "property", "value")
    assert isinstance(requires_multiple, ConditionMultiple)
    assert requires_multiple.checkCondition() is True
