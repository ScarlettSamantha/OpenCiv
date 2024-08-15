from openciv.gameplay.effect import Effects, Effect
from openciv.engine.managers.i18n import T_TranslationOrStr


class Leader:
    def __init__(self, name: T_TranslationOrStr, icon: str, description: T_TranslationOrStr) -> None:
        self.name: T_TranslationOrStr = name
        self.icon: str = icon
        self.description: T_TranslationOrStr = description

        self._effects: Effects = Effects()

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
