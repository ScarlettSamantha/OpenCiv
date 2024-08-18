from __future__ import annotations
from openciv.gameplay.cultures.core.subs._base import BaseCoreSubtree
from openciv.engine.managers.i18n import _t


class Technocracy(BaseCoreSubtree):
    def __init__(self, *args, **kwargs):
        super().__init__(
            key="core.culture.subtrees.technocracy",
            name=_t("content.culture.subtrees.core.technocracy.name"),
            description=_t("content.culture.subtrees.core.technocracy.description"),
            *args,
            **kwargs,
        )

    def register_civics(self):
        from openciv.gameplay.cultures.core.expert_governance import ExpertGovernance
        from openciv.gameplay.cultures.core.scientific_management import ScientificManagement
        from openciv.gameplay.cultures.core.innovation_focus import InnovationFocus
        from openciv.gameplay.cultures.core.data_driven_policy import DataDrivenPolicy
        from openciv.gameplay.cultures.core.efficient_administration import EfficientAdministration
        from openciv.gameplay.cultures.core.meritocracy import Meritocracy
        from openciv.engine.requires import RequiresCivicComplete

        expert_governance = ExpertGovernance()
        self.add_civic(expert_governance)

        scientific_management = ScientificManagement()
        scientific_management.requires = [RequiresCivicComplete(expert_governance)]
        self.add_civic(scientific_management)

        innovation_focus = InnovationFocus()
        innovation_focus.requires = [RequiresCivicComplete(expert_governance)]
        self.add_civic(innovation_focus)

        data_driven_policy = DataDrivenPolicy()
        data_driven_policy.requires = [
            RequiresCivicComplete(scientific_management),
            RequiresCivicComplete(innovation_focus),
        ]
        self.add_civic(data_driven_policy)

        efficient_administration = EfficientAdministration()
        efficient_administration.requires = [RequiresCivicComplete(data_driven_policy)]
        self.add_civic(efficient_administration)

        meritocracy = Meritocracy()
        meritocracy.requires = [RequiresCivicComplete(efficient_administration)]
        self.add_civic(meritocracy)
