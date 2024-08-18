from __future__ import annotations
class BaseException(Exception):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
