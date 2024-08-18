from __future__ import annotations
from openciv.engine.exceptions._base_exception import BaseException


class SaveException(BaseException):
    pass


class SaveFailureException(SaveException):
    pass


class SaveRestorationFailure(SaveException):
    pass


class SaveRestoreObjectPropertyNotFoundException(SaveRestorationFailure):
    pass


class SaveRestoreObjectPropertyObjectInvalidRestoreStateException(SaveRestorationFailure):
    pass


class SaveRestoreObjectNotRestorableException(SaveRestorationFailure):
    pass


class SaveRestorationRestoreTypeInvalidException(SaveRestorationFailure):
    pass


class SavePropertyIsNotAValidSaveableTypeException(SaveFailureException):
    pass


class SavePropertyIsObjectButNotSaveAbleException(SaveFailureException):
    pass
