from openciv.gameplay.culture import Civic
from openciv.engine.managers.i18n import _t


class EconomicIntegration(Civic):
    def __init__(self, *args, **kwargs):
        super().__init__(
            key="core.culture.civics.economic_integration",
            name=_t("content.culture.civics.core.economic_integration.name"),
            description=_t("content.culture.civics.core.economic_integration.description"),
            *args,
            **kwargs,
        )
