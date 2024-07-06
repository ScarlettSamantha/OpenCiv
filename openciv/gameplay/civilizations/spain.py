from openciv.gameplay.civilization import Civilization
from openciv.gameplay.effect import Effect
from openciv.engine.managers.i18n import _t


class Spain(Civilization):
    def __init__(self):
        super().__init__(name=_t("civilization.spain.name"), description=_t("civilization.spain.description"))

        self._loadable = True
        self.icon = "icons/rome.png"

    def register_effects(self):
        self.add_effect(
            Effect("civilization.rome.effects.civ_bonus_1", target=Effect.PLAYER_CURRENT, domain=Effect.PLAYER)
        )

    def register_leaders(self):
        from openciv.gameplay.leaders.isabella import Isabella
        from openciv.gameplay.leaders.charles_v import CharlesV
        from openciv.gameplay.leaders.charles_iii import CharlesIII
        from openciv.gameplay.leaders.james import James
        from openciv.gameplay.leaders.phillip import Phillip

        self.add_leader(Isabella())
        self.add_leader(CharlesV())
        self.add_leader(CharlesIII())
        self.add_leader(James())
        self.add_leader(Phillip())
