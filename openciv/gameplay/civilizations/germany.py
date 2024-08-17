from openciv.gameplay.civilization import Civilization

from openciv.engine.managers.i18n import t_


class Germany(Civilization):
    def __init__(self):
        super().__init__(name=t_("civilization.germany.name"), description=t_("civilization.germany.description"))

        self._loadable = True
        self.icon = "icons/rome.png"

    def register_effects(self):
        pass

    def register_leaders(self):
        from openciv.gameplay.leaders.otto import Otto
        from openciv.gameplay.leaders.wilhelm import Wilhelm

        self.add_leader(Otto())
        self.add_leader(Wilhelm())
