from __future__ import annotations
from openciv.gameplay.culture import Civic
from openciv.engine.managers.i18n import _t


class CollectiveOwnership(Civic):
    def __init__(self, *args, **kwargs):
        super().__init__(
            key="core.culture.civics.collective_ownership",
            name=_t("content.culture.civics.core.collective_ownership.name"),
            description=_t("content.culture.civics.core.collective_ownership.description"),
            *args,
            **kwargs,
        )
