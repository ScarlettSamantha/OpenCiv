from openciv.gameplay.greats.core.scientists._base import CoreBaseGreatScientist
from openciv.engine.managers.i18n import _t


class Tesla(CoreBaseGreatScientist):
    def __init__(self):
        super().__init__(
            key="core.scientists.tesla",
            name=_t("content.greats.core.people.tesla.name"),
            description=_t("content.greats.core.people.tesla.description"),
            cost=100,
        )
