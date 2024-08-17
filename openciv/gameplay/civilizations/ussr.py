from openciv.gameplay.civilization import Civilization

from openciv.engine.managers.i18n import t_


class Ussr(Civilization):
    def __init__(self):
        super().__init__(name=t_("civilization.ussr.name"), description=t_("civilization.ussr.description"))

        self._loadable = True
        self.icon = "icons/rome.png"

    def register_effects(self):
        pass

    def register_leaders(self):
        from openciv.gameplay.leaders.lenin import Lenin
        from openciv.gameplay.leaders.gorbashov import Gorbashov
        from openciv.gameplay.leaders.peter import Peter

        self.add_leader(Lenin())
        self.add_leader(Gorbashov())
        self.add_leader(Peter())
