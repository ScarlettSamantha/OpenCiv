from openciv.gameplay.culture import Civic
from openciv.engine.managers.i18n import _t


class EvidenceBasedPolicy(Civic):
    def __init__(self, *args, **kwargs):
        super().__init__(
            key="core.culture.civics.evidence_based_policy",
            name=_t("content.culture.civics.core.evidence_based_policy.name"),
            description=_t("content.culture.civics.core.evidence_based_policy.description"),
            *args,
            **kwargs,
        )
