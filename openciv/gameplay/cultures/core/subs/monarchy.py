from __future__ import annotations
from openciv.gameplay.cultures.core.subs._base import BaseCoreSubtree
from openciv.engine.managers.i18n import _t


class Monarchy(BaseCoreSubtree):
    def __init__(self):
        super().__init__(
            key="core.culture.subtrees.monarchy",
            name=_t("content.culture.subtrees.core.monarchy.name"),
            description=_t("content.culture.subtrees.core.monarchy.description"),
        )

    def register_civics(self):
        from openciv.gameplay.cultures.core.hereditary_rule import HereditaryRule
        from openciv.gameplay.cultures.core.divine_right import DivineRight
        from openciv.gameplay.cultures.core.nobility_system import NobilitySystem
        from openciv.gameplay.cultures.core.feudal_obligations import FeudalObligations
        from openciv.gameplay.cultures.core.centralized_authority import CentralizedAuthority
        from openciv.gameplay.cultures.core.royal_patronage import RoyalPatronage
        from openciv.engine.requires import RequiresCivicComplete

        hereditary_rule = HereditaryRule()
        self.add_civic(hereditary_rule)

        divine_right = DivineRight()
        divine_right.requires = [RequiresCivicComplete(hereditary_rule)]
        self.add_civic(divine_right)

        nobility_system = NobilitySystem()
        nobility_system.requires = [RequiresCivicComplete(divine_right)]
        self.add_civic(nobility_system)

        feudal_obligations = FeudalObligations()
        feudal_obligations.requires = [RequiresCivicComplete(nobility_system)]
        self.add_civic(feudal_obligations)

        centralized_authority = CentralizedAuthority()
        centralized_authority.requires = [RequiresCivicComplete(feudal_obligations)]
        self.add_civic(centralized_authority)

        royal_patronage = RoyalPatronage()
        royal_patronage.requires = [RequiresCivicComplete(centralized_authority)]
        self.add_civic(royal_patronage)
