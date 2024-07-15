from openciv.gameplay.culture import Civic
from openciv.engine.managers.i18n import _t


class CentralizedPower(Civic):
    def __init__(self, *args, **kwargs):
        super().__init__(
            key="core.culture.civics.centralized_power",
            name=_t("content.culture.civics.core.centralized_power.name"),
            description=_t("content.culture.civics.core.centralized_power.description"),
            *args,
            **kwargs,
        )
