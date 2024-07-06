from openciv.gameplay.civilization import Civilization
from openciv.gameplay.effect import Effect
from openciv.engine.managers.i18n import _t


class Ussr(Civilization):
    def __init__(self):
        super().__init__(name=_t("civilization.ussr.name"), description=_t("civilization.ussr.description"))

        self._loadable = True
        self.icon = "icons/rome.png"

    def register_effects(self):
        self.add_effect(
            Effect("civilization.rome.effects.civ_bonus_1", target=Effect.PLAYER_CURRENT, domain=Effect.PLAYER)
        )

    def register_leaders(self):
        from openciv.gameplay.leaders.lenin import Lenin
        from openciv.gameplay.leaders.gorbashov import Gorbashov
        from openciv.gameplay.leaders.peter import Peter

        self.add_leader(Lenin())
        self.add_leader(Gorbashov())
        self.add_leader(Peter())
