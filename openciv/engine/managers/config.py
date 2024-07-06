import io
import json

from openciv.engine.exceptions.config_exception import ConfigEntryNotFound
from typing import Any


class Config:
    def __init__(self, path):
        self.path = path
        self._data = {}

    def load(self):
        fp = io.open(self.path, "r")
        self._data = json.loads(fp.read())

    def get(self, key: str, default: Any = None, fail_if_not_found: bool = True):
        data = self._data
        splits = key.split(".")
        for i, level in enumerate(splits):
            if level in list(data.keys()):
                data = data[level]
                if i == (len(splits) - 1):
                    return data
            else:
                if fail_if_not_found:
                    raise ConfigEntryNotFound(f"Failed to find {key}")
                else:
                    return default
