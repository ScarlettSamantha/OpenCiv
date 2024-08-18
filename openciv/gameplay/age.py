from __future__ import annotations
from openciv.engine.managers.i18n import T_TranslationOrStrOrNone
from typing import Tuple


class Age:
    def __init__(
        self,
        key: T_TranslationOrStrOrNone,
        name: T_TranslationOrStrOrNone,
        description: T_TranslationOrStrOrNone,
        color: Tuple[int, int, int, int] | None,
    ) -> None:
        self.key: T_TranslationOrStrOrNone = key
        self.name: T_TranslationOrStrOrNone = name
        self.description: T_TranslationOrStrOrNone = description
        self.color: Tuple[int, int, int, int] | None = color
