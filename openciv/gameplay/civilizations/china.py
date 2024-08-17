from __future__ import annotations

from openciv.gameplay.civilization import Civilization

from openciv.engine.managers.i18n import t_


class China(Civilization):
    def __init__(self):
        super().__init__(name=t_("civilization.china.name"), description=t_("civilization.china.description"))

        self._loadable = True
        self.icon = "icons/rome.png"

    def register_effects(self):
        pass

    def register_leaders(self):
        from openciv.gameplay.leaders.qin_shi_huang import QinShiHuang
        from openciv.gameplay.leaders.kublai import Kublai

        self.add_leader(QinShiHuang())
        self.add_leader(Kublai())
