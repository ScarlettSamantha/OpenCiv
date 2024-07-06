from openciv.gameplay.civilization import Civilization
from openciv.gameplay.effect import Effect
from openciv.engine.managers.i18n import _t


class China(Civilization):
    def __init__(self):
        super().__init__(name=_t("civilization.china.name"), description=_t("civilization.china.description"))

        self._loadable = True
        self.icon = "icons/rome.png"

    def register_effects(self):
        self.add_effect(
            Effect("civilization.rome.effects.civ_bonus_1", target=Effect.PLAYER_CURRENT, domain=Effect.PLAYER)
        )

    def register_leaders(self):
        from openciv.gameplay.leaders.qin_shi_huang import QinShiHuang
        from openciv.gameplay.leaders.kublai import Kublai

        self.add_leader(QinShiHuang())
        self.add_leader(Kublai())
