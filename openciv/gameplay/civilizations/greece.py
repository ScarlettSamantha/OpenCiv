from __future__ import annotations
from openciv.gameplay.civilization import Civilization

from openciv.engine.managers.i18n import t_


class Greece(Civilization):
    def __init__(self):
        super().__init__(name=t_("civilization.greece.name"), description=t_("civilization.greece.description"))

        self._loadable = True
        self.icon = "icons/rome.png"

    def register_effects(self):
        pass

    def register_leaders(self):
        from openciv.gameplay.leaders.leonidas import Leonidas
        from openciv.gameplay.leaders.alexander import Alexander

        self.add_leader(Leonidas())
        self.add_leader(Alexander())
