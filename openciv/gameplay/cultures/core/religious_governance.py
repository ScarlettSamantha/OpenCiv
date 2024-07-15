from openciv.gameplay.culture import Civic
from openciv.engine.managers.i18n import _t


class ReligiousGovernance(Civic):
    def __init__(self, *args, **kwargs):
        super().__init__(
            key="core.culture.civics.religious_governance",
            name=_t("content.culture.civics.core.religious_governance.name"),
            description=_t("content.culture.civics.core.religious_governance.description"),
            *args,
            **kwargs,
        )
