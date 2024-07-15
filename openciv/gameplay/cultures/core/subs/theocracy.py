from openciv.gameplay.cultures.core.subs._base import BaseCoreSubtree
from openciv.engine.managers.i18n import _t


class Theocracy(BaseCoreSubtree):
    def __init__(self, *args, **kwargs):
        super().__init__(
            key="core.culture.subtrees.theocracy",
            name=_t("content.culture.subtrees.core.theocracy.name"),
            description=_t("content.culture.subtrees.core.theocracy.description"),
            *args,
            **kwargs,
        )

    def register_civics(self):
        from openciv.gameplay.cultures.core.religious_law import ReligiousLaw
        from openciv.gameplay.cultures.core.clerical_rule import ClericalRule
        from openciv.gameplay.cultures.core.moral_policing import MoralPolicing
        from openciv.gameplay.cultures.core.faith_based_education import FaithBasedEducation
        from openciv.gameplay.cultures.core.divine_governance import DivineGovernance
        from openciv.gameplay.cultures.core.religious_unity import ReligiousUnity
        from openciv.engine.requires import RequiresCivicComplete

        religious_law = ReligiousLaw()
        self.add_civic(religious_law)

        clerical_rule = ClericalRule()
        clerical_rule.requires = [RequiresCivicComplete(religious_law)]
        self.add_civic(clerical_rule)

        moral_policing = MoralPolicing()
        moral_policing.requires = [RequiresCivicComplete(religious_law)]
        self.add_civic(moral_policing)

        faith_based_education = FaithBasedEducation()
        faith_based_education.requires = [RequiresCivicComplete(clerical_rule), RequiresCivicComplete(moral_policing)]
        self.add_civic(faith_based_education)

        divine_governance = DivineGovernance()
        divine_governance.requires = [RequiresCivicComplete(faith_based_education)]
        self.add_civic(divine_governance)

        religious_unity = ReligiousUnity()
        religious_unity.requires = [RequiresCivicComplete(divine_governance)]
        self.add_civic(religious_unity)
