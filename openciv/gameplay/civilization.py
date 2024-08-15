from typing import Self, List
from openciv.gameplay.effect import Effects, Effect
from openciv.gameplay.leader import Leader
from abc import abstractmethod


class Civilization:
    def __init__(self, name: str, description: str) -> None:
        self.name: str = name
        self.icon: str | None = None
        self._loadable = False
        self.description: str = description
        self._leaders: List[Leader] = []

        self._effects: Effects = Effects()

        # Init registers
        self.register_effects()
        self.register_leaders()

    def effects(self) -> Effects:
        return self._effects

    def add_effect(self, effect: Effect) -> None:
        self._effects.add(effect=effect, key_or_auto=str(effect.name))

    def add_leader(self, leader: Leader) -> None:
        self.leaders.append(leader)

    @property
    def leaders(self) -> List[Leader]:
        return self._leaders

    @leaders.setter
    def leaders(self, leaders: List[Leader]) -> None:
        self._leaders = leaders

    @abstractmethod
    def register_effects(self) -> None:
        pass

    @abstractmethod
    def register_leaders(Self) -> None:
        pass

    def __str__(self) -> str:
        leader_name_list: List[str] = []
        for leader in self.leaders:
            leader_name_list.append(leader.name if leader.name else "Unknown")
        leaders: str = ", ".join(leader_name_list)
        return f"{self.name} - {self.description} <{leaders}>"

    def __call__(self) -> Self:
        return self
