from openciv.gameplay.citizen import Citizen
from openciv.engine.mixins.callbacks import CallbacksMixin

from typing import List


class Citizens(CallbacksMixin):
    def __init__(self):
        super().__init__()
        self._citizens: List[Citizen] = []
        self.register_citizen_events()

    def register_citizen_events(self):
        self._declare_event("on_birth")

    def add(self, value: Citizen, as_birth: bool = True):
        self._citizens.append(value)
        if as_birth:
            super(CallbacksMixin).trigger_callback("on_birth", value)

    def remove(self, value: Citizen | int = 1, as_death: bool = True):
        if isinstance(value, int):
            for i in range(value):
                self._citizens.pop()
        elif isinstance(value, Citizen):
            self._citizens.remove(value)

        if as_death:
            super(CallbacksMixin).trigger_callback("on_death", value)

    def reset(self):
        self._citizens: List[Citizen] = []

    def create(self, num: int = 1, *args, **kwargs):
        def _create(self, *args, **kwargs):
            self.add(Citizen(*args, **kwargs))

        for i in range(num):
            _create(self, *args, **kwargs)

    def __add__(self, value: Citizen):
        self.add(value)

    def __len__(self) -> int:
        return len(self._citizens)
