from openciv.gameplay.cultures.core.subs._base import BaseCoreSubtree
from openciv.engine.managers.i18n import _t


class Salvery(BaseCoreSubtree):
    def __init__(self):
        super().__init__(
            key="core.culture.subtrees.slavery",
            name=_t("content.culture.subtrees.core.slavery.name"),
            description=_t("content.culture.subtrees.core.slavery.description"),
        )

    def register_civics(self):
        from openciv.gameplay.cultures.core.forced_labor import ForcedLabor
        from openciv.gameplay.cultures.core.ownership_rights import OwnershipRights
        from openciv.gameplay.cultures.core.labor_exploitation import LaborExploitation
        from openciv.gameplay.cultures.core.social_hierarchy import SocialHierarchy
        from openciv.gameplay.cultures.core.oppression import Oppression
        from openciv.gameplay.cultures.core.economic_dependence import EconomicDependence
        from openciv.engine.requires import RequiresCivicComplete

        forced_labor = ForcedLabor()
        self.add_civic(forced_labor)

        ownership_rights = OwnershipRights()
        ownership_rights.requires = [RequiresCivicComplete(forced_labor)]
        self.add_civic(ownership_rights)

        labor_exploitation = LaborExploitation()
        labor_exploitation.requires = [RequiresCivicComplete(forced_labor)]
        self.add_civic(labor_exploitation)

        social_hierarchy = SocialHierarchy()
        social_hierarchy.requires = [
            RequiresCivicComplete(ownership_rights),
            RequiresCivicComplete(labor_exploitation),
        ]
        self.add_civic(social_hierarchy)

        oppression = Oppression()
        oppression.requires = [RequiresCivicComplete(social_hierarchy)]
        self.add_civic(oppression)

        economic_dependence = EconomicDependence()
        economic_dependence.requires = [RequiresCivicComplete(oppression)]
        self.add_civic(economic_dependence)
