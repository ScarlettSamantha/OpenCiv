from openciv.engine.managers.i18n import T_TranslationOrStr
from typing import Tuple


class Age:
    def __init__(
        self,
        key: T_TranslationOrStr,
        name: T_TranslationOrStr,
        description: T_TranslationOrStr,
        color: Tuple[int, int, int, int],
    ):
        self.key: T_TranslationOrStr = key
        self.name: T_TranslationOrStr = name
        self.description: T_TranslationOrStr = description
        self.color: Tuple[int, int, int, int] = color
