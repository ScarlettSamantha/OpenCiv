from __future__ import annotations

from openciv.gameplay.civilization import Civilization

from openciv.engine.managers.i18n import t_


class Spain(Civilization):
    def __init__(self):
        super().__init__(name=t_("civilization.spain.name"), description=t_("civilization.spain.description"))

        self._loadable = True
        self.icon = "icons/rome.png"

    def register_effects(self):
        pass

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
