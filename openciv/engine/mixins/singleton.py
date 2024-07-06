from abc import ABC, abstractmethod
from typing import Type, TypeVar, Optional

T = TypeVar("T", bound="Singleton")


class Singleton(ABC):
    __instance: Optional[T] = None

    @abstractmethod
    def __setup__(self, *args, **kwargs) -> None:
        """Method to set up the singleton instance."""
        pass

    def __new__(cls: Type[T], *args, **kwargs) -> T:
        if cls.__instance is None:
            cls.__instance = super(Singleton, cls).__new__(cls)
            cls.__instance.__setup__(*args, **kwargs)
        return cls.__instance

    @classmethod
    def _get_instance(cls: Type[T], *args, **kwargs) -> T:
        if cls.__instance is None:
            cls.__instance = cls.__new__(cls, *args, **kwargs)
        return cls.__instance

    @classmethod
    def _set_instance(cls: Type[T], instance: T) -> T:
        cls.__instance = instance
        return cls.__instance
