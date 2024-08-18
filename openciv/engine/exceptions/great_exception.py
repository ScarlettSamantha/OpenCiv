from __future__ import annotations
from openciv.engine.exceptions._base_exception import BaseException


class GreatException(BaseException):
    pass


class GreatLoadingException(GreatException):
    pass


class GreatLoadingFolderNotFoundException(GreatLoadingException):
    pass


class GreatPersonNotLoaded(GreatException):
    pass


class GreatPersonTreeNotLoaded(GreatException):
    pass
