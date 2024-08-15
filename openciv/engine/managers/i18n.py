from __future__ import annotations

import io
import pathlib
import json

from os import PathLike
from pathlib import Path

from typing import Union, Dict, Any
from openciv.engine.managers.log import LogManager
from openciv.engine.saving import SaveAble

from openciv.engine.exceptions.i18n_exception import (
    I18NLoadException,
    I18NDecodeException,
    I18NTranslationNotFound,
    I18NNotLoadedException,
)


class _i18n:
    def __init__(
        self,
        base_path: str | Path | PathLike[Any],
        language: str | None = None,
        auto_load: bool = True,
        manager: Any = None,
    ) -> None:
        self.base_path: str | Path | PathLike[Any] = base_path
        self._data: Dict[str, Dict[Any, Any]] = {}
        self.manager: Any = manager

        self.default_language = "en_EN"
        self.language: str = language if language else self.default_language

        if auto_load and self.language_exists(language=self.language):
            self.load_language(language=self.language)

    def generate_path(self, path: PathLike[Any] | str) -> PathLike[Any] | str:
        base_path: Path | PathLike[Any] | str = (
            Path(self.base_path) if not isinstance(self.base_path, PathLike) else self.base_path
        )
        if isinstance(path, PathLike):
            return base_path / path  # type: ignore
        elif isinstance(path, str):  # type: ignore
            return base_path / path  # type: ignore

    def language_exists(self, language: str) -> bool:
        path = pathlib.Path(self.generate_path(path=f"{language}.json"))
        return path.exists()

    def load_file(self, path: str) -> None:
        try:
            f = io.open(file=path, mode="r")
        except FileNotFoundError:
            raise I18NLoadException(f"Failed to open {path}")
        try:
            self._data.update(json.loads(f.read()))
        except json.JSONDecodeError:
            raise I18NDecodeException(f"Failed to decode {path}")

    def current_language(self) -> str:
        return self.language

    def set_current_language(self, language: str) -> None:
        self.language = language

    def load_language(self, language: str):
        self.load_file(path=str(self.generate_path(path=f"{language}.json")))

    def lookup(self, key: str, default: Any | None = None, fail_on_not_found: bool = False) -> str:
        LogManager.get_instance().engine.debug(msg=f"Looking up {key}")
        data = self._data
        splits: list[str] = key.split(sep=".")
        for i, level in enumerate(splits):
            if level in list(data.keys()):
                data: Dict[Any, Any] = data[level]
                # If we are at the end of the key return the data
                if i == (len(splits) - 1):
                    return str(data)
            else:
                if fail_on_not_found:
                    raise I18NTranslationNotFound(f"Key {key} not found")
                return key
        if default is None and fail_on_not_found:
            raise I18NTranslationNotFound(f"Key {key} not found")
        return key if default is None else default


i18n: None | _i18n = None


def set_i18n(i18n_instance: _i18n) -> None:
    global i18n
    i18n = i18n_instance


class Translation(SaveAble):
    def __init__(self, key: str) -> None:
        SaveAble.__init__(self)
        self.key: str = key
        self._setup_saveable()

    def __repr__(self) -> str:
        self_str: str = str(self) if i18n else "[!unloaded i18n engine!]"
        return f"Translation({self.key}) -> {self_str}"

    def __str__(self) -> str:
        if i18n is None:
            raise I18NNotLoadedException(
                "I18n not loaded, there is probibly not an instance of the manager earlie enough in your load order."
            )
        try:
            # We want to handle the fail in the translation object so we can handle it on a higher level.
            return i18n.lookup(key=self.key, fail_on_not_found=True)
        except I18NTranslationNotFound:
            return self.key

    def __hash__(self) -> int:
        return hash(self.key)

    def __eq__(self, other: Translation) -> bool:
        return self.key == other.key


_t = Translation
t_ = Translation
T_TranslationOrStr = Union[Translation, str]
