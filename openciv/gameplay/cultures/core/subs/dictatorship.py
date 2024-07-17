from openciv.gameplay.cultures.core.subs._base import BaseCoreSubtree
from openciv.engine.managers.i18n import _t


class Dictatorship(BaseCoreSubtree):
    def __init__(self):
        super().__init__(
            key="core.culture.subtrees.dictatorship",
            name=_t("content.culture.subtrees.core.dictatorship.name"),
            description=_t("content.culture.subtrees.core.dictatorship.description"),
        )

    def register_civics(self):
        from openciv.gameplay.cultures.core.autocratic_rule import AutocraticRule
        from openciv.gameplay.cultures.core.state_surveillance import StateSurveillance
        from openciv.gameplay.cultures.core.censorship import Censorship
        from openciv.gameplay.cultures.core.repression import Repression
        from openciv.gameplay.cultures.core.propaganda import Propaganda
        from openciv.gameplay.cultures.core.centralized_power import CentralizedPower
        from openciv.engine.requires import RequiresCivicComplete

        autocratic_rule = AutocraticRule()
        self.add_civic(autocratic_rule)

        state_surveillance = StateSurveillance()
        state_surveillance.requires = [RequiresCivicComplete(autocratic_rule)]
        self.add_civic(state_surveillance)

        censorship = Censorship()
        censorship.requires = [RequiresCivicComplete(autocratic_rule)]
        self.add_civic(censorship)

        repression = Repression()
        repression.requires = [RequiresCivicComplete(state_surveillance), RequiresCivicComplete(censorship)]
        self.add_civic(repression)

        propaganda = Propaganda()
        propaganda.requires = [RequiresCivicComplete(repression)]
        self.add_civic(propaganda)

        centralized_power = CentralizedPower()
        centralized_power.requires = [RequiresCivicComplete(propaganda)]
        self.add_civic(centralized_power)
