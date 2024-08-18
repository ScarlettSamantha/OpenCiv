from __future__ import annotations
from openciv.gameplay.culture import Civic
from openciv.engine.managers.i18n import _t


class ParticipatoryGovernance(Civic):
    def __init__(self, *args, **kwargs):
        super().__init__(
            key="core.culture.civics.participatory_governance",
            name=_t("content.culture.civics.core.participatory_governance.name"),
            description=_t("content.culture.civics.core.participatory_governance.description"),
            *args,
            **kwargs,
        )
