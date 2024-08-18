from __future__ import annotations
from openciv.gameplay.culture import Civic
from openciv.engine.managers.i18n import _t


class CorporateGovernance(Civic):
    def __init__(self, *args, **kwargs):
        super().__init__(
            key="core.culture.civics.corporate_governance",
            name=_t("content.culture.civics.core.corporate_governance.name"),
            description=_t("content.culture.civics.core.corporate_governance.description"),
            *args,
            **kwargs,
        )
