from openciv.gameplay.culture import Civic
from openciv.engine.managers.i18n import _t


class SelfGovernance(Civic):
    def __init__(self, *args, **kwargs):
        super().__init__(
            key="core.culture.civics.self_governance",
            name=_t("content.culture.civics.core.self_governance.name"),
            description=_t("content.culture.civics.core.self_governance.description"),
            *args,
            **kwargs,
        )
