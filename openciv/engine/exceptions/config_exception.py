from openciv.engine.exceptions._base_exception import BaseException


class ConfigException(BaseException):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class ConfigEntryNotFound(ConfigException):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
