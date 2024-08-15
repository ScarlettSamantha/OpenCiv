from __future__ import annotations
from typing import Any, Type

from openciv.engine.managers.i18n import T_TranslationOrStr
from openciv.gameplay.promotion import PromotionTree


class UnitBaseClass:
    def __init__(
        self,
        key: str,
        name: T_TranslationOrStr,
        description: T_TranslationOrStr,
        icon: str | None,
        promotion_tree: Type[PromotionTree],
        *args: Any,
        **kwargs: Any,
    ):
        self.key: str = key
        self.name: T_TranslationOrStr = name
        self.description: T_TranslationOrStr = description
        self.icon: str | None = icon
        self.promotion_tree: Type[PromotionTree] = promotion_tree
