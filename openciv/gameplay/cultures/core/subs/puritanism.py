from openciv.gameplay.cultures.core.subs._base import BaseCoreSubtree
from openciv.engine.managers.i18n import _t


class Puritanism(BaseCoreSubtree):
    def __init__(self):
        super().__init__(
            key="core.culture.subtrees.puritanism",
            name=_t("content.culture.subtrees.core.puritanism.name"),
            description=_t("content.culture.subtrees.core.puritanism.description"),
        )

    def register_civics(self):
        from openciv.gameplay.cultures.core.religious_discipline import ReligiousDiscipline
        from openciv.gameplay.cultures.core.moral_purity import MoralPurity
        from openciv.gameplay.cultures.core.community_surveillance import CommunitySurveillance
        from openciv.gameplay.cultures.core.simplified_living import SimplifiedLiving
        from openciv.gameplay.cultures.core.religious_governance import ReligiousGovernance
        from openciv.gameplay.cultures.core.moral_legislation import MoralLegislation
        from openciv.engine.requires import RequiresCivicComplete

        religious_discipline = ReligiousDiscipline()
        self.add_civic(religious_discipline)

        moral_purity = MoralPurity()
        moral_purity.requires = [RequiresCivicComplete(religious_discipline)]
        self.add_civic(moral_purity)

        community_surveillance = CommunitySurveillance()
        community_surveillance.requires = [RequiresCivicComplete(religious_discipline)]
        self.add_civic(community_surveillance)

        simplified_living = SimplifiedLiving()
        simplified_living.requires = [
            RequiresCivicComplete(moral_purity),
            RequiresCivicComplete(community_surveillance),
        ]
        self.add_civic(simplified_living)

        religious_governance = ReligiousGovernance()
        religious_governance.requires = [RequiresCivicComplete(simplified_living)]
        self.add_civic(religious_governance)

        moral_legislation = MoralLegislation()
        moral_legislation.requires = [RequiresCivicComplete(religious_governance)]
        self.add_civic(moral_legislation)
