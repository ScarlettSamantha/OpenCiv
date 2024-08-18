from __future__ import annotations
from openciv.gameplay.civilization import Civilization

from openciv.engine.managers.i18n import t_


class AmericanEmpire(Civilization):
    def __init__(self):
        super().__init__(
            name=t_("civilization.american_empire.name"), description=t_("civilization.american_empire.description")
        )

        self._loadable = True
        self.icon = "icons/rome.png"

    def register_effects(self):
        pass

    def register_leaders(self):
        from openciv.gameplay.leaders.abraham_lincoln import AbrahamLincoln
        from openciv.gameplay.leaders.fdr import FDR
        from openciv.gameplay.leaders.kamehameha import Kamehameha
        from openciv.gameplay.leaders.sitting_bull import SittingBull

        self.add_leader(AbrahamLincoln())
        self.add_leader(FDR())
        self.add_leader(Kamehameha())
        self.add_leader(SittingBull())
