from __future__ import annotations
from openciv.gameplay.culture import Civic
from openciv.engine.managers.i18n import _t


class ExpertGovernance(Civic):
    def __init__(self, *args, **kwargs):
        super().__init__(
            key="core.culture.civics.expert_governance",
            name=_t("content.culture.civics.core.expert_governance.name"),
            description=_t("content.culture.civics.core.expert_governance.description"),
            *args,
            **kwargs,
        )
