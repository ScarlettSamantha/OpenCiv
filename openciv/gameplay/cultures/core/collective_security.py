from openciv.gameplay.culture import Civic
from openciv.engine.managers.i18n import _t


class CollectiveSecurity(Civic):
    def __init__(self, *args, **kwargs):
        super().__init__(
            key="core.culture.civics.collective_security",
            name=_t("content.culture.civics.core.collective_security.name"),
            description=_t("content.culture.civics.core.collective_security.description"),
            *args,
            **kwargs,
        )
