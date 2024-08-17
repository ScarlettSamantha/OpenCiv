from openciv.gameplay.civilization import Civilization

from openciv.engine.managers.i18n import t_


class Ottoman(Civilization):
    def __init__(self):
        super().__init__(name=t_("civilization.ottoman.name"), description=t_("civilization.ottoman.description"))

        self._loadable = True
        self.icon = "icons/rome.png"

    def register_effects(self):
        pass

    def register_leaders(self):
        from openciv.gameplay.leaders.attaturk import Attaturk
        from openciv.gameplay.leaders.suleiman import Suleiman

        self.add_leader(Attaturk())
        self.add_leader(Suleiman())
