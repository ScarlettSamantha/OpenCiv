from __future__ import annotations
from openciv.gameplay.greats.core.scientists._base import CoreBaseGreatScientist
from openciv.engine.managers.i18n import _t


class Einstein(CoreBaseGreatScientist):
    def __init__(self):
        super().__init__(
            key="core.scientists.einstein",
            name=_t("content.greats.core.people.einstein.name"),
            description=_t("content.greats.core.people.einstein.description"),
            cost=100,
        )
