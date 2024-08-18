from __future__ import annotations
from openciv.gameplay.civilization import Civilization

from openciv.engine.managers.i18n import t_


class Japan(Civilization):
    def __init__(self):
        super().__init__(name=t_("civilization.japan.name"), description=t_("civilization.japan.description"))

        self._loadable = True
        self.icon = "icons/rome.png"

    def register_effects(self):
        pass

    def register_leaders(self):
        from openciv.gameplay.leaders.tokugawa import Tokugawa
        from openciv.gameplay.leaders.meiji import Meiji
        from openciv.gameplay.leaders.taisho import Taisho

        self.add_leader(Tokugawa())
        self.add_leader(Meiji())
        self.add_leader(Taisho())
