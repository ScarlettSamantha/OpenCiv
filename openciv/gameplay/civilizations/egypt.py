from openciv.gameplay.civilization import Civilization

from openciv.engine.managers.i18n import t_


class Egypt(Civilization):
    def __init__(self):
        super().__init__(name=t_("civilization.egypt.name"), description=t_("civilization.egypt.description"))

        self._loadable = True
        self.icon = "icons/rome.png"

    def register_effects(self):
        pass

    def register_leaders(self):
        from openciv.gameplay.leaders.ramesses import Ramesses
        from openciv.gameplay.leaders.cleopatra import Cleopatra

        self.add_leader(Ramesses())
        self.add_leader(Cleopatra())
