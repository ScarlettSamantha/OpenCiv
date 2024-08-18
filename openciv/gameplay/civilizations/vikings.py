from __future__ import annotations
from openciv.gameplay.civilization import Civilization

from openciv.engine.managers.i18n import t_


class Vikings(Civilization):
    def __init__(self):
        super().__init__(name=t_("civilization.vikings.name"), description=t_("civilization.vikings.description"))

        self._loadable = True
        self.icon = "icons/rome.png"

    def register_effects(self):
        pass

    def register_leaders(self):
        from openciv.gameplay.leaders.cnut import Cnut
        from openciv.gameplay.leaders.ragnar import Ragnar
        from openciv.gameplay.leaders.herald import Herald

        self.add_leader(Cnut())
        self.add_leader(Ragnar())
        self.add_leader(Herald())
