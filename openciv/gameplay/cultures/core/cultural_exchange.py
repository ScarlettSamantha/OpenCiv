from openciv.gameplay.culture import Civic
from openciv.engine.managers.i18n import _t


class CulturalExchange(Civic):
    def __init__(self, *args, **kwargs):
        super().__init__(
            key="core.culture.civics.cultural_exchange",
            name=_t("content.culture.civics.core.cultural_exchange.name"),
            description=_t("content.culture.civics.core.cultural_exchange.description"),
            *args,
            **kwargs,
        )
