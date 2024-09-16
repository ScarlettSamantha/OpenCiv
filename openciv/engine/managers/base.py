from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any, Type
from openciv.engine.mixins.singleton import Singleton, T


class BaseManager:
    def __init__(self, parent: "BaseManager" = None):
        self.parent = parent

    def parent(self) -> "BaseManager":
        return self.parent

    def setParent(self, parent: "BaseManager") -> None:
        self.parent = parent


class BaseSingletonManager(Singleton):
    """
    Singleton manager base class. By transitive (?) rule, to enforce singularity, can only have a singleton parent.
    """
    @abstractmethod
    def __setup__(self, *args: Any, **kwargs: Any):
        pass

    def is_root_manager(self) -> bool:
        return self._parent is None

    def parent(self) -> "BaseSingletonManager|None":
        return self._parent
    
    def setParent(self, parent: "BaseSingletonManager") -> None:
        self._parent = parent
