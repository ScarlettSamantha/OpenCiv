from openciv.gameplay.civilization import Civilization
from openciv.gameplay.effect import Effect
from openciv.engine.managers.i18n import _t


class Japan(Civilization):
    def __init__(self):
        super().__init__(name=_t("civilization.japan.name"), description=_t("civilization.japan.description"))

        self._loadable = True
        self.icon = "icons/rome.png"

    def register_effects(self):
        self.add_effect(
            Effect("civilization.rome.effects.civ_bonus_1", target=Effect.PLAYER_CURRENT, domain=Effect.PLAYER)
        )

    def register_leaders(self):
        from openciv.gameplay.leaders.tokugawa import Tokugawa
        from openciv.gameplay.leaders.meiji import Meiji
        from openciv.gameplay.leaders.taisho import Taisho

        self.add_leader(Tokugawa())
        self.add_leader(Meiji())
        self.add_leader(Taisho())
