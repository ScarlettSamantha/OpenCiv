from openciv.engine.exceptions._base_exception import BaseException


class ResourceException(BaseException):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class ResourceTypeException(ResourceException):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class ResourceMathException(ResourceException):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
