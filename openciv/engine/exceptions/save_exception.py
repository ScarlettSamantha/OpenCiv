from openciv.engine.exceptions._base_exception import BaseException


class SaveException(BaseException):
    pass


class SaveFailureException(SaveException):
    pass


class SaveRestorationFailure(SaveException):
    pass


class SaveRestoreObjectPropertyNotFoundException(SaveRestorationFailure):
    pass


class SaveRestoreObjectNotRestorableException(SaveRestorationFailure):
    pass


class SaveRestorationRestoreTypeInvalidException(SaveRestorationFailure):
    pass
