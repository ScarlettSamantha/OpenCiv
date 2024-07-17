from openciv.gameplay.cultures.core.subs._base import BaseCoreSubtree
from openciv.engine.managers.i18n import _t


class Democracy(BaseCoreSubtree):
    def __init__(self):
        super().__init__(
            key="core.culture.subtrees.democracy",
            name=_t("content.culture.subtrees.core.democracy.name"),
            description=_t("content.culture.subtrees.core.democracy.description"),
        )

    def register_civics(self):
        from openciv.gameplay.cultures.core.electoral_process import ElectoralProcess
        from openciv.gameplay.cultures.core.rule_of_law import RuleOfLaw
        from openciv.gameplay.cultures.core.separation_of_powers import SeparationOfPowers
        from openciv.gameplay.cultures.core.human_rights import HumanRights
        from openciv.gameplay.cultures.core.participatory_governance import ParticipatoryGovernance
        from openciv.gameplay.cultures.core.transparent_government import TransparentGovernment
        from openciv.engine.requires import RequiresCivicComplete

        electoral_process = ElectoralProcess()
        self.add_civic(electoral_process)

        rule_of_law = RuleOfLaw()
        rule_of_law.requires = [RequiresCivicComplete(electoral_process)]
        self.add_civic(rule_of_law)

        separation_of_powers = SeparationOfPowers()
        separation_of_powers.requires = [RequiresCivicComplete(rule_of_law)]
        self.add_civic(separation_of_powers)

        human_rights = HumanRights()
        human_rights.requires = [RequiresCivicComplete(rule_of_law)]
        self.add_civic(human_rights)

        participatory_governance = ParticipatoryGovernance()
        participatory_governance.requires = [
            RequiresCivicComplete(separation_of_powers),
            RequiresCivicComplete(human_rights),
        ]
        self.add_civic(participatory_governance)

        transparent_government = TransparentGovernment()
        transparent_government.requires = [RequiresCivicComplete(participatory_governance)]
        self.add_civic(transparent_government)
