from __future__ import annotations

from openciv.engine.exceptions._base_exception import BaseException
from typing import Any


class ResourceException(BaseException):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)  # type: ignore


class ResourceTypeException(ResourceException):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class ResourceMathException(ResourceException):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
