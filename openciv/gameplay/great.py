from __future__ import annotations
from typing import List, NoReturn, ForwardRef, Tuple
from openciv.engine.managers.i18n import T_TranslationOrStr
from openciv.engine.exceptions.great_exception import GreatPersonTreeNotLoaded
from openciv.engine.saving import SaveAble
from openciv.engine.managers.log import LogManager
from openciv.gameplay.effect import Effects
from openciv.gameplay.resource import Resource
from openciv.gameplay.resources.core.mechanics._base import BaseGreatMechanicResource


class Great(SaveAble):
    def __init__(
        self,
        key: str,
        name: T_TranslationOrStr,
        description: T_TranslationOrStr,
        resource_type_required: Resource | None | Tuple | BaseGreatMechanicResource | List = None,
        cost: float = 0.0,
        *args,
        **kwargs,
    ):
        super().__init__(*args, **kwargs)
        self.key: str = key
        self.name: T_TranslationOrStr = name
        self.description: T_TranslationOrStr = description
        self.cost: float = cost
        self.bought: bool = False
        self.on_map: bool = False
        self.effects: Effects = Effects()
        self.resource_type_required: Resource | None | Tuple | BaseGreatMechanicResource | List = resource_type_required
        self._setup_saveable()


class GreatsTree(SaveAble):
    def __init__(
        self,
        key: str,
        name: T_TranslationOrStr,
        description: T_TranslationOrStr,
        greats: List[Great] = [],
        points: float = 0.0,
        *args,
        **kwargs,
    ):
        super().__init__(*args, **kwargs)
        self.key: str = key
        self.greats: List[Great] = greats
        self.points: float = points
        self.name: T_TranslationOrStr = name
        self.description: T_TranslationOrStr = description
        self.effects_on_finish: Effects = Effects()
        self._setup_saveable()

    def buy_great(self, great: Great) -> Great:
        self.points -= great.points
        LogManager.get_instance().gameplay.debug(f"Bought Great {great.__class__.__name__} for {great.points} points")
        return great

    def add_great(self, great: Great) -> NoReturn:
        self.greats.append(great)
        LogManager.get_instance().gameplay.debug(f"Added Great {great.__class__.__name__} to {self.name}")

    def remove_great(self, great: Great) -> NoReturn:
        self.greats.remove(great)
        LogManager.get_instance().gameplay.debug(f"Removed Great {great.__class__.__name__} from {self.name}")

    def __add__(self, b: int | float | Great) -> ForwardRef("GreatsTree"):
        if isinstance(b, Great):
            self.add_great(b)
            return self
        LogManager.get_instance().gameplay.debug(f"Adding {b.__class__.__name__} points to {self.name}")
        self.points += float(b)
        return self

    def __radd__(self, b: int | float | Great) -> ForwardRef("GreatsTree"):
        return self.__add__(b)

    def __sub__(self, b: int | float | Great) -> ForwardRef("GreatsTree"):
        if isinstance(b, Great):
            self.remove_great(b)
            return self
        LogManager.get_instance().gameplay.debug(f"Subtracting {b} points from {self.name}")
        self.points -= float(b)
        return self

    def __rsub__(self, b: int | float | Great) -> ForwardRef("GreatsTree"):
        return self.__sub__(b)


class Greats:
    def __init__(self, loaded_great_trees: List[GreatsTree] = []):
        self.loaded_trees: List[GreatsTree] = loaded_great_trees

    def _check_tree_exists(self, tree: str, exception_on_fail: bool = True):
        if tree not in self.categories:
            if exception_on_fail:
                raise GreatPersonTreeNotLoaded(f"Great Person Tree {tree} not loaded")
            return False
        return True

    def addTree(self, tree: str):
        self._check_tree_exists(tree, True)
        self.loaded_trees.append(tree)

    def addPoint(self, tree: str, amount: int | float):
        self._check_tree_exists(tree, True)
        self.loaded_trees[tree] += amount

    def decreasePoints(self, tree: str, amount: int | float):
        self._check_tree_exists(tree, True)
        self.loaded_trees[tree] -= amount

    def setPoints(self, tree: str, amount: int | float):
        self._check_tree_exists(tree, True)
        self.loaded_trees[tree] = amount
