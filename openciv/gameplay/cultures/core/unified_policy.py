from openciv.gameplay.culture import Civic
from openciv.engine.managers.i18n import _t


class UnifiedPolicy(Civic):
    def __init__(self, *args, **kwargs):
        super().__init__(
            key="core.culture.civics.unified_policy",
            name=_t("content.culture.civics.core.unified_policy.name"),
            description=_t("content.culture.civics.core.unified_policy.description"),
            *args,
            **kwargs,
        )
