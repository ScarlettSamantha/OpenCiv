from __future__ import annotations

from openciv.gameplay.effect import Effects, Effect
from openciv.engine.managers.i18n import T_TranslationOrStr
from openciv.engine.saving import SaveAble


class Leader(SaveAble):
    def __init__(
        self, key: str, name: T_TranslationOrStr, description: T_TranslationOrStr, icon: str | None = None
    ) -> None:
        super().__init__()
        self.key: str = key
        self.name: T_TranslationOrStr = name
        self.icon: str | None = icon
        self.description: T_TranslationOrStr = description

        self._effects: Effects = Effects()
        self._setup_saveable()

    @property
    def effects(self) -> Effects:
        return self._effects

    @effects.setter
    def effects(self, effects: Effects) -> None:
        self._effects = effects

    def add_effect(self, effect: Effect) -> None:
        self._effects.add(effect=effect)

    def get_effects(self) -> Effects:
        return self._effects
