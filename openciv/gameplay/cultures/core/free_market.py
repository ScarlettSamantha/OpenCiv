from __future__ import annotations
from openciv.gameplay.culture import Civic
from openciv.engine.managers.i18n import _t


class FreeMarket(Civic):
    def __init__(self, *args, **kwargs):
        super().__init__(
            key="core.culture.civics.free_market",
            name=_t("content.culture.civics.core.free_market.name"),
            description=_t("content.culture.civics.core.free_market.description"),
            *args,
            **kwargs,
        )
