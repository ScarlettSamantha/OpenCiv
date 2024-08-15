from __future__ import annotations

from typing import List, Any, Union, Iterable
from openciv.engine.exceptions.condition_exception import ConditionObjectPropertyDoesNotExist
from openciv.engine.saving import SaveAble
from openciv.engine.mixins.callbacks import CallbacksMixin
from collections.abc import Callable


class Condition(SaveAble, CallbacksMixin):
    def __init__(self, obj: object, property: str, required_value: Any, *args: Any, **kwargs: Any) -> None:
        SaveAble.__init__(self, *args, **kwargs)
        CallbacksMixin.__init__(self, *args, **kwargs)

        self.obj: object = obj
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
            return _property_ref() == self.required_value  # type: ignore

        return _property_ref == self.required_value

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}[obj={self.obj}, property={self.property}, required_value={self.required_value}] -> {self.checkCondition()}"


class ConditionMultiple(Condition):
    def __init__(self, conditions: List[Condition], *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self.conditions: List[Condition] = conditions

    def checkCondition(self) -> bool:
        for condition in self.conditions:
            if not condition.checkCondition():
                return False
        return True


class Requires(Condition):
    def __init__(self, *args: Any, **kwargs: Any):
        super().__init__(*args, **kwargs)


class RequiresMultiple(ConditionMultiple):
    def __init__(self, *args: Any, **kwargs: Any):
        super().__init__(*args, **kwargs)

    @classmethod
    def convert_from_list(cls, conditions: T_Requires) -> RequiresMultiple:
        return cls(conditions=conditions)


class RequiresCivicComplete(Requires):
    def __init__(self, civic: Civic, *args: Any, **kwargs: Any):  # type: ignore
        super().__init__(obj=civic, property="completed", required_value=True, *args, **kwargs)


class RequiresCivicsComplete(RequiresMultiple):
    def __init__(self, civics: List[Civic], *args: Any, **kwargs: Any):  # type: ignore
        super().__init__(*args, **kwargs)
        for civic in civics:  # type: ignore
            _instance: RequiresCivicComplete = RequiresCivicComplete(civic=civic)  # type: ignore
            self.conditions.append(_instance)


class RequriesSubtreeCompelete(Requires):
    def __init__(self, subtree: CultureSubtree, *args: Any, **kwargs: Any) -> None:  # type: ignore
        super().__init__(obj=subtree, property="is_completed", required_value=True, *args, **kwargs)


class RequiresSubtreesComplete(RequiresMultiple):
    def __init__(self, subtrees: List[CultureSubtree], *args: Any, **kwargs: Any):  # type: ignore
        super().__init__(*args, **kwargs)
        for subtree in subtrees:  # type: ignore
            _instance: RequriesSubtreeCompelete = RequriesSubtreeCompelete(subtree=subtree)  # type: ignore
            self.conditions.append(_instance)


class RequiresPromotionComplete(Requires):
    def __init__(self, promotion: Promotion, *args: Any, **kwargs: Any):  # type: ignore
        super().__init__(obj=promotion, property="aquired", required_value=True, *args, **kwargs)


class RequiresPromotionsComplete(RequiresMultiple):
    def __init__(self, promotions: List[Promotion], *args: Any, **kwargs: Any) -> None:  # type: ignore
        super().__init__(*args, **kwargs)
        for promotion in promotions:  # type: ignore
            _instance: RequiresPromotionComplete = RequiresPromotionComplete(promotion=promotion)  # type: ignore
            self.conditions.append(_instance)


class RequiresPromotionTreeUnlocked(Requires):
    def __init__(self, promotion_tree: PromotionTree, *args: Any, **kwargs: Any) -> None:  # type: ignore
        super().__init__(obj=promotion_tree, property="unlocked", required_value=True, *args, **kwargs)


class RequiresPromotionTreesUnlocked(RequiresMultiple):
    def __init__(self, promotion_trees: List[PromotionTree], *args: Any, **kwargs: Any) -> None:  # type: ignore
        super().__init__(*args, **kwargs)
        for promotion_tree in promotion_trees:  # type: ignore
            _instance: RequiresPromotionTreeUnlocked = RequiresPromotionTreeUnlocked(promotion_tree=promotion_tree)  # type: ignore
            self.conditions.append(_instance)


T_Requires = Union[Requires, RequiresMultiple, Iterable[Requires], None]

# Forward references without import
Civic = "Civic"
CultureSubtree = "CultureSubtree"
Promotion = "Promotion"
PromotionTree = "PromotionTree"
