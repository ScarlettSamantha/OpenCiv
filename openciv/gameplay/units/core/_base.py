from __future__ import annotations
from typing import Any

from openciv.gameplay.units.baseunit import BaseUnit


class CoreBaseUnit(BaseUnit):
    pass


class CoreBaseCivilianUnit(CoreBaseUnit):
    def __init__(self, *args: Any, **kwargs: Any):
        super().__init__(*args, **kwargs)


class CoreBaseMilitaryUnit(CoreBaseUnit):
    pass
