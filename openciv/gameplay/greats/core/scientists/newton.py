from __future__ import annotations
from openciv.gameplay.greats.core.scientists._base import CoreBaseGreatScientist
from openciv.engine.managers.i18n import _t


class Newton(CoreBaseGreatScientist):
    def __init__(self):
        super().__init__(
            key="core.scientists.newton",
            name=_t("content.greats.core.people.newton.name"),
            description=_t("content.greats.core.people.newton.description"),
            cost=100,
        )
