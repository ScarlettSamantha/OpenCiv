from openciv.gameplay.effects import Effects
from abc import abstractmethod


class Civilization:
    def __init__(self, name: str, description: str):
        self.name: str = name
        self.icon: str = None
        self._loadable = False
        self.description: str = description
        self.leaders: list = []

        self._effects: Effects = Effects()

        # Init registers
        self.register_effects()
        self.register_leaders()

    def effects(self):
        return self._effects

    def add_effect(self, effect):
        self._effects.add(effect, effect.name)

    def add_leader(self, leader):
        self.leaders.append(leader)

    def leaders(self):
        return self.leaders

    @abstractmethod
    def register_effects(self):
        pass

    @abstractmethod
    def register_leaders(Self):
        pass

    def __str__(self):
        leaders = ", ".join([leader.name for leader in self.leaders])
        return f"{self.name} - {self.description} <{leaders}>"

    def __call__(self):
        return self
