from openciv.gameplay.civilization import Civilization
from openciv.gameplay.effect import Effect
from openciv.engine.managers.i18n import _t


class Egypt(Civilization):
    def __init__(self):
        super().__init__(name=_t("civilization.egypt.name"), description=_t("civilization.egypt.description"))

        self._loadable = True
        self.icon = "icons/rome.png"

    def register_effects(self):
        self.add_effect(
            Effect("civilization.rome.effects.civ_bonus_1", target=Effect.PLAYER_CURRENT, domain=Effect.PLAYER)
        )

    def register_leaders(self):
        from openciv.gameplay.leaders.ramesses import Ramesses
        from openciv.gameplay.leaders.cleopatra import Cleopatra

        self.add_leader(Ramesses())
        self.add_leader(Cleopatra())
