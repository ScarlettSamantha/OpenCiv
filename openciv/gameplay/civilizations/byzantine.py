from openciv.gameplay.civilization import Civilization


class Byzantine(Civilization):
    def __init__(self):
        super().__init__(name="civilization.byzantine.name", description="civilization.byzantine.description")

        self._loadable = True
        self.icon = "icons/rome.png"

    def register_effects(self):
        pass

    def register_leaders(self):
        from openciv.gameplay.leaders.justinian import Justinian
        from openciv.gameplay.leaders.constantine import Constantine

        self.add_leader(Justinian())
        self.add_leader(Constantine())
