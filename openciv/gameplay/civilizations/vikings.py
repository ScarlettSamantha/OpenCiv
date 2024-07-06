from openciv.gameplay.civilization import Civilization
from openciv.gameplay.effect import Effect
from openciv.engine.managers.i18n import _t


class Vikings(Civilization):
    def __init__(self):
        super().__init__(name=_t("civilization.vikings.name"), description=_t("civilization.vikings.description"))

        self._loadable = True
        self.icon = "icons/rome.png"

    def register_effects(self):
        self.add_effect(
            Effect("civilization.rome.effects.civ_bonus_1", target=Effect.PLAYER_CURRENT, domain=Effect.PLAYER)
        )

    def register_leaders(self):
        from openciv.gameplay.leaders.cnut import Cnut
        from openciv.gameplay.leaders.ragnar import Ragnar
        from openciv.gameplay.leaders.herald import Herald

        self.add_leader(Cnut())
        self.add_leader(Ragnar())
        self.add_leader(Herald())
