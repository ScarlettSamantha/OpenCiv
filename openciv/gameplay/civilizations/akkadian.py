from openciv.gameplay.civilization import Civilization
from openciv.gameplay.effect import Effect
from openciv.engine.managers.i18n import _t


class Akkadian(Civilization):
    def __init__(self):
        super().__init__(name=_t("civilization.akkadian.name"), description=_t("civilization.akkadian.description"))

        self._loadable = True
        self.icon = "icons/rome.png"

    def register_effects(self):
        self.add_effect(
            Effect("civilization.rome.effects.civ_bonus_1", target=Effect.PLAYER_CURRENT, domain=Effect.PLAYER)
        )

    def register_leaders(self):
        from openciv.gameplay.leaders.sargon import Sargon
        from openciv.gameplay.leaders.naram_sin import NaramSin

        self.add_leader(Sargon())
        self.add_leader(NaramSin())
