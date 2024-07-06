from openciv.gameplay.civilization import Civilization
from openciv.gameplay.effect import Effect
from openciv.engine.managers.i18n import _t


class France(Civilization):
    def __init__(self):
        super().__init__(name=_t("civilization.france.name"), description=_t("civilization.france.description"))

        self._loadable = True
        self.icon = "icons/rome.png"

    def register_effects(self):
        self.add_effect(
            Effect("civilization.rome.effects.civ_bonus_1", target=Effect.PLAYER_CURRENT, domain=Effect.PLAYER)
        )

    def register_leaders(self):
        from openciv.gameplay.leaders.napoleon import Napoleon
        from openciv.gameplay.leaders.charlemagne import Charlemagne
        from openciv.gameplay.leaders.de_gaulle import DeGaulle
        from openciv.gameplay.leaders.louis import Louis

        self.add_leader(Napoleon())
        self.add_leader(Charlemagne())
        self.add_leader(DeGaulle())
        self.add_leader(Louis())
