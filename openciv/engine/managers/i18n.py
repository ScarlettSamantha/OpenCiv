from os import PathLike
from pathlib import Path
import io
import pathlib
import json

from typing import Union
from openciv.engine.managers.log import LogManager

from openciv.engine.exceptions.i18n_exception import (
    I18NLoadException,
    I18NDecodeException,
    I18NTranslationNotFound,
    I18NNotLoadedException,
)


class _i18n:
    def __init__(self, base_path: str | Path | PathLike, language: str = None, auto_load: bool = True, manager=None):
        self.base_path = base_path
        self._data = {}
        self.manager = manager

        self.default_language = "en_EN"
        self.language = language if language else self.default_language

        if auto_load and self.language_exists(self.language):
            self.load_language(self.language)

    def generate_path(self, path: str) -> PathLike:
        base_path = Path(self.base_path) if not isinstance(self.base_path, PathLike) else self.base_path
        return str(base_path / path)

    def language_exists(self, language: str) -> bool:
        path = pathlib.Path(self.generate_path(f"{language}.json"))
        return path.exists()

    def load_file(self, path: str):
        try:
            f = io.open(path, "r")
        except FileNotFoundError:
            raise I18NLoadException(f"Failed to open {path}")
        try:
            self._data.update(json.loads(f.read()))
        except json.JSONDecodeError:
            raise I18NDecodeException(f"Failed to decode {path}")

    def current_language(self) -> str:
        return self.language

    def set_current_language(self, language: str):
        self.language = language

    def load_language(self, language: str):
        self.load_file(self.generate_path(f"{language}.json"))

    def lookup(self, key: str, fail_on_not_found: bool = False) -> str:
        LogManager._get_instance().engine.debug(f"Looking up {key}")
        data = self._data
        splits = key.split(".")
        for i, level in enumerate(splits):
            if level in list(data.keys()):
                data = data[level]
                if i == (len(splits) - 1):
                    return data
            else:
                if fail_on_not_found:
                    raise I18NTranslationNotFound(f"Key {key} not found")
                return key


i18n = None


def set_i18n(i18n_instance: i18n) -> None:
    global i18n
    i18n = i18n_instance


class Translation:
    def __init__(self, key: str):
        self._key = key

    @property
    def key(self):
        return self._key

    @key.setter
    def key(self, value) -> None:
        self._key = value

    def __repr__(self):
        self_str = str(self) if i18n else "[!unloaded i18n engine!]"
        return f"Translation({self.key}) -> {self_str}"

    def __str__(self):
        if i18n is None:
            raise I18NNotLoadedException(
                "I18n not loaded, there is probibly not an instance of the manager earlie enough in your load order."
            )
        try:
            # We want to handle the fail in the translation object so we can handle it on a higher level.
            return i18n.lookup(self.key, fail_on_not_found=True)
        except I18NTranslationNotFound:
            return self.key


_t = Translation
T_TranslationOrStr = Union[Translation, str]
