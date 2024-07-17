from openciv.gameplay.cultures.core.subs._base import BaseCoreSubtree
from openciv.engine.managers.i18n import _t


class Rationalism(BaseCoreSubtree):
    def __init__(self, *args, **kwargs):
        super().__init__(
            key="core.culture.subtrees.rationalism",
            name=_t("content.culture.subtrees.core.rationalism.name"),
            description=_t("content.culture.subtrees.core.rationalism.description"),
            *args,
            **kwargs,
        )

    def register_civics(self):
        from openciv.gameplay.cultures.core.reason_and_logic import ReasonAndLogic
        from openciv.gameplay.cultures.core.scientific_inquiry import ScientificInquiry
        from openciv.gameplay.cultures.core.secular_governance import SecularGovernance
        from openciv.gameplay.cultures.core.education_reform import EducationReform
        from openciv.gameplay.cultures.core.evidence_based_policy import EvidenceBasedPolicy
        from openciv.gameplay.cultures.core.philosophical_discourse import PhilosophicalDiscourse
        from openciv.engine.requires import RequiresCivicComplete

        reason_and_logic = ReasonAndLogic()
        self.add_civic(reason_and_logic)

        scientific_inquiry = ScientificInquiry()
        scientific_inquiry.requires = [RequiresCivicComplete(reason_and_logic)]
        self.add_civic(scientific_inquiry)

        secular_governance = SecularGovernance()
        secular_governance.requires = [RequiresCivicComplete(reason_and_logic)]
        self.add_civic(secular_governance)

        education_reform = EducationReform()
        education_reform.requires = [
            RequiresCivicComplete(scientific_inquiry),
            RequiresCivicComplete(secular_governance),
        ]
        self.add_civic(education_reform)

        evidence_based_policy = EvidenceBasedPolicy()
        evidence_based_policy.requires = [RequiresCivicComplete(education_reform)]
        self.add_civic(evidence_based_policy)

        philosophical_discourse = PhilosophicalDiscourse()
        philosophical_discourse.requires = [RequiresCivicComplete(evidence_based_policy)]
        self.add_civic(philosophical_discourse)
