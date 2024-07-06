from openciv.gameplay.civilization import Civilization
from openciv.gameplay.effect import Effect
from openciv.engine.managers.i18n import _t


class Persia(Civilization):
    def __init__(self):
        super().__init__(name=_t("civilization.persia.name"), description=_t("civilization.persia.description"))

        self._loadable = True
        self.icon = "icons/rome.png"

    def register_effects(self):
        self.add_effect(
            Effect("civilization.rome.effects.civ_bonus_1", target=Effect.PLAYER_CURRENT, domain=Effect.PLAYER)
        )

    def register_leaders(self):
        from openciv.gameplay.leaders.darius import Darius
        from openciv.gameplay.leaders.xerxes import Xerxes
        from openciv.gameplay.leaders.nebuchadnezzar import Nebuchadnezzar

        self.add_leader(Darius())
        self.add_leader(Xerxes())
        self.add_leader(Nebuchadnezzar())
