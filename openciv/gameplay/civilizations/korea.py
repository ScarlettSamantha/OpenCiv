from __future__ import annotations
from openciv.gameplay.civilization import Civilization

from openciv.engine.managers.i18n import t_


class Korea(Civilization):
    def __init__(self):
        super().__init__(name=t_("civilization.korea.name"), description=t_("civilization.korea.description"))

        self._loadable = True
        self.icon = "icons/rome.png"

    def register_effects(self):
        pass

    def register_leaders(self):
        from openciv.gameplay.leaders.sejon import Sejon
        from openciv.gameplay.leaders.goi import Goi

        self.add_leader(Sejon())
        self.add_leader(Goi())
