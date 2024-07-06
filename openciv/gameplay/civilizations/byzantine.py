from openciv.gameplay.civilization import Civilization
from openciv.gameplay.effect import Effect


class Byzantine(Civilization):
    def __init__(self):
        super().__init__(name="civilization.byzantine.name", description="civilization.byzantine.description")

        self._loadable = True
        self.icon = "icons/rome.png"

    def register_effects(self):
        self.add_effect(
            Effect("civilization.rome.effects.civ_bonus_1", target=Effect.PLAYER_CURRENT, domain=Effect.PLAYER)
        )

    def register_leaders(self):
        from openciv.gameplay.leaders.justinian import Justinian
        from openciv.gameplay.leaders.constantine import Constantine

        self.add_leader(Justinian())
        self.add_leader(Constantine())
