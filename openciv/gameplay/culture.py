from openciv.engine.saving import SaveAble
from openciv.engine.managers.i18n import T_TranslationOrStr
from openciv.engine.mixins.callbacks import CallbacksMixin
from typing import ForwardRef, List, NoReturn, List
from openciv.engine.requires import Requires
from abc import abstractmethod


class Civic(SaveAble, CallbacksMixin):
    def __init__(
        self, key: str, name: T_TranslationOrStr, description: T_TranslationOrStr, _cost: int = 0, *args, **kwargs
    ):
        SaveAble.__init__(self, *args, **kwargs)
        CallbacksMixin.__init__(self, *args, **kwargs)

        self.key: str = key
        self.name: T_TranslationOrStr = name
        self.description: T_TranslationOrStr = description

        self.requires: List[ForwardRef("Civic")] = []
        self._cost: int = _cost
        self._progress: int = 0
        self._completed: bool = False
        self.requires: List[Requires] = []

        self._setup_saveable()
        self.declare_callbacks()

    def declare_callbacks(self):
        self._declare_event("on_progress")
        self._declare_event("on_complete")

    @property
    def completed(self) -> bool:
        return self._completed

    @completed.setter
    def completed(self, value: bool) -> NoReturn:
        self._completed = value
        self.trigger_callback("on_complete")

    @property
    def cost(self) -> int:
        return self._cost

    @cost.setter
    def cost(self, value: int | float) -> NoReturn:
        if isinstance(value, float):
            self._cost = round(value)
        else:
            self._cost = value

    @property
    def progress(self) -> int:
        return self._progress

    @progress.setter
    def progress(self, value: int | float) -> NoReturn:
        if isinstance(value, float):
            self._progress = round(value)
        else:
            self._progress = value

        self.trigger_callback("on_progress")

        if self._progress >= self.cost:
            self.completed = True

    def is_requires_completed(self) -> bool:
        return all(requirement.checkCondition() for requirement in self.requires)

    def __add__(self, other: int):
        self.progress += other
        return self

    def __sub__(self, other: int):
        self.progress -= other
        return self

    def __mul__(self, other: int):
        self.progress = round(self.cost, other)
        return self

    def __truediv__(self, other: int):
        self.progress = round(self.clost / other)
        return self

    def add_requirement(self, culture: ForwardRef("Culture")) -> NoReturn:
        self.requires.append(culture)


class CultureSubtree:
    def __init__(self, key: str, name: T_TranslationOrStr, description: T_TranslationOrStr, *args, **kwargs):
        self.key: str = key
        self.name: T_TranslationOrStr = name
        self.description: T_TranslationOrStr = description

        self.civics: List[Civic] = []

    @abstractmethod
    def register_civics(self) -> NoReturn:
        pass

    def add_civic(self, civic: Civic) -> NoReturn:
        self.civics.append(civic)

    def is_completed(self) -> bool:
        return all(civic.completed for civic in self.cultures)


class CultureTree:
    def __init__(self, key: str, name: T_TranslationOrStr, description: T_TranslationOrStr, *args, **kwargs):
        self.key: str = key
        self.name: T_TranslationOrStr = name
        self.description: T_TranslationOrStr = description

        self.subtrees: List[CultureSubtree] = []
        self.register_subtrees()

    @abstractmethod
    def register_subtrees(self) -> NoReturn:
        pass

    def add_subtree(self, subtree: CultureSubtree) -> NoReturn:
        self.subtrees.append(subtree)
