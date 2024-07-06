from openciv.gameplay.civilization import Civilization
from openciv.gameplay.effect import Effect
from openciv.engine.managers.i18n import _t


class LowCountries(Civilization):
    def __init__(self):
        super().__init__(
            name=_t("civilization.low_countries.name"), description=_t("civilization.low_countries.description")
        )

        self._loadable = True
        self.icon = "icons/rome.png"

    def register_effects(self):
        self.add_effect(
            Effect("civilization.rome.effects.civ_bonus_1", target=Effect.PLAYER_CURRENT, domain=Effect.PLAYER)
        )

    def register_leaders(self):
        from openciv.gameplay.leaders.willem import Willem
        from openciv.gameplay.leaders.ambiorix import Ambiorix

        self.add_leader(Willem())
        self.add_leader(Ambiorix())
