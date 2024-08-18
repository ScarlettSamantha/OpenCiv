from __future__ import annotations
from openciv.engine.exceptions.gameplay_exception import GameplayException


class EffectException(GameplayException):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class EffectDoesNotExist(EffectException):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class EffectAlreadyExists(EffectException):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class EffectCannotBeBoughtOff(EffectException):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
