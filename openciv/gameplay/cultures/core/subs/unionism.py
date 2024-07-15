from openciv.gameplay.cultures.core.subs._base import BaseCoreSubtree
from openciv.engine.managers.i18n import _t


class Unionism(BaseCoreSubtree):
    def __init__(self):
        super().__init__(
            key="core.culture.subtrees.unionism",
            name=_t("content.culture.subtrees.core.unionism.name"),
            description=_t("content.culture.subtrees.core.unionism.description"),
        )

    def register_civics(self):
        from openciv.gameplay.cultures.core.cooperative_governance import CooperativeGovernance
        from openciv.gameplay.cultures.core.shared_sovereignty import SharedSovereignty
        from openciv.gameplay.cultures.core.economic_integration import EconomicIntegration
        from openciv.gameplay.cultures.core.cultural_exchange import CulturalExchange
        from openciv.gameplay.cultures.core.collective_security import CollectiveSecurity
        from openciv.gameplay.cultures.core.unified_policy import UnifiedPolicy
        from openciv.engine.requires import RequiresCivicComplete

        cooperative_governance = CooperativeGovernance()
        self.add_civic(cooperative_governance)

        shared_sovereignty = SharedSovereignty()
        shared_sovereignty.requires = [RequiresCivicComplete(cooperative_governance)]
        self.add_civic(shared_sovereignty)

        economic_integration = EconomicIntegration()
        economic_integration.requires = [RequiresCivicComplete(shared_sovereignty)]
        self.add_civic(economic_integration)

        cultural_exchange = CulturalExchange()
        cultural_exchange.requires = [RequiresCivicComplete(economic_integration)]
        self.add_civic(cultural_exchange)

        collective_security = CollectiveSecurity()
        collective_security.requires = [RequiresCivicComplete(cultural_exchange)]
        self.add_civic(collective_security)

        unified_policy = UnifiedPolicy()
        unified_policy.requires = [RequiresCivicComplete(collective_security)]
        self.add_civic(unified_policy)
