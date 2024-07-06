from openciv.gameplay.civilization import Civilization
from openciv.gameplay.effect import Effect
from openciv.engine.managers.i18n import _t


class Rome(Civilization):
    def __init__(self):
        super().__init__(name=_t("civilization.rome.name"), description=_t("civilization.rome.description"))

        self._loadable = True
        self.icon = "icons/rome.png"

    def register_effects(self):
        self.add_effect(
            Effect("civilization.rome.effects.civ_bonus_1", target=Effect.PLAYER_CURRENT, domain=Effect.PLAYER)
        )

    def register_leaders(self):
        from openciv.gameplay.leaders.ceasar import Ceasar
        from openciv.gameplay.leaders.augustus import Augustus

        self.add_leader(Ceasar())
        self.add_leader(Augustus())
