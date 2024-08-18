from __future__ import annotations
from openciv.gameplay.exceptions.gameplay_exception import GameplayException


class ImprovementException(GameplayException):
    pass


class ImprovementUpgradeException(ImprovementException):
    pass
