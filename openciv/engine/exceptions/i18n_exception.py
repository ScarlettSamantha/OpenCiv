from openciv.engine.exceptions.resource_exception import ResourceException


class I18NException(ResourceException):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class I18NLoadException(I18NException):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class I18NDecodeException(I18NException):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class I18NTranslationNotFound(I18NException):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class I18NNotLoadedException(I18NException):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
