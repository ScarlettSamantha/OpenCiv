from openciv.gameplay.civilization import Civilization

from openciv.engine.managers.i18n import t_


class Persia(Civilization):
    def __init__(self):
        super().__init__(name=t_("civilization.persia.name"), description=t_("civilization.persia.description"))

        self._loadable = True
        self.icon = "icons/rome.png"

    def register_effects(self):
        pass

    def register_leaders(self):
        from openciv.gameplay.leaders.darius import Darius
        from openciv.gameplay.leaders.xerxes import Xerxes
        from openciv.gameplay.leaders.nebuchadnezzar import Nebuchadnezzar

        self.add_leader(Darius())
        self.add_leader(Xerxes())
        self.add_leader(Nebuchadnezzar())
