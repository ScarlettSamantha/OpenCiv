from typing import List, Any, ForwardRef
from openciv.engine.exceptions.condition_exception import ConditionObjectPropertyDoesNotExist
from openciv.engine.saving import SaveAble
from openciv.engine.mixins.callbacks import CallbacksMixin
from collections.abc import Callable


class Condition(SaveAble, CallbacksMixin):
    def __init__(self, obj: object, property: str, required_value: Any, *args, **kwargs) -> None:
        SaveAble.__init__(self, *args, **kwargs)
        CallbacksMixin.__init__(self, *args, **kwargs)

        self.obj: obj = obj
        self.property: str = property
        self.required_value = required_value

        self._setup_saveable()

    def checkCondition(self) -> bool:
        if not hasattr(self.obj, self.property):
            raise ConditionObjectPropertyDoesNotExist(
                f"Object[{self.obj.__class__.__name__}] does not have property[{self.property}]"
            )

        _property_ref = getattr(self.obj, self.property)
        # If the property is a function, call it and compare the result to the required value
        if isinstance(_property_ref, Callable):
            return _property_ref() == self.required_value

        return _property_ref == self.required_value

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}[obj={self.obj}, property={self.property}, required_value={self.required_value}] -> {self.checkCondition()}"


class ConditionMultiple(Condition):
    def __init__(self, conditions: List[Condition], *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.conditions: List[Condition] = conditions

    def checkCondition(self) -> bool:
        for condition in self.conditions:
            if not condition.checkCondition():
                return False
        return True


class Requires(Condition):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class RequiresMultiple(ConditionMultiple):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
