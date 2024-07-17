from openciv.gameplay.cultures.core.subs._base import BaseCoreSubtree
from openciv.engine.managers.i18n import _t


class Corporatocracy(BaseCoreSubtree):
    def __init__(
        self,
    ):
        super().__init__(
            key="core.culture.subtrees.corporatocracy",
            name=_t("content.culture.subtrees.core.corporatocracy.name"),
            description=_t("content.culture.subtrees.core.corporatocracy.description"),
        )

    def register_civics(self):
        from openciv.gameplay.cultures.core.corporate_influence import CorporateInfluence
        from openciv.gameplay.cultures.core.lobbying_power import LobbyingPower
        from openciv.gameplay.cultures.core.business_privileges import BusinessPrivileges
        from openciv.gameplay.cultures.core.economic_focus import EconomicFocus
        from openciv.gameplay.cultures.core.regulatory_capture import RegulatoryCapture
        from openciv.gameplay.cultures.core.corporate_governance import CorporateGovernance
        from openciv.engine.requires import RequiresCivicComplete

        corporate_influence = CorporateInfluence()
        self.add_civic(corporate_influence)

        lobbying_power = LobbyingPower()
        lobbying_power.requires = [RequiresCivicComplete(corporate_influence)]
        self.add_civic(lobbying_power)

        business_privileges = BusinessPrivileges()
        business_privileges.requires = [RequiresCivicComplete(corporate_influence)]
        self.add_civic(business_privileges)

        economic_focus = EconomicFocus()
        economic_focus.requires = [RequiresCivicComplete(lobbying_power), RequiresCivicComplete(business_privileges)]
        self.add_civic(economic_focus)

        regulatory_capture = RegulatoryCapture()
        regulatory_capture.requires = [RequiresCivicComplete(economic_focus)]
        self.add_civic(regulatory_capture)

        corporate_governance = CorporateGovernance()
        corporate_governance.requires = [RequiresCivicComplete(regulatory_capture)]
        self.add_civic(corporate_governance)
