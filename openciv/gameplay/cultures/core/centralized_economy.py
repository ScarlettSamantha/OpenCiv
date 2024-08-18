from __future__ import annotations
from openciv.gameplay.culture import Civic
from openciv.engine.managers.i18n import _t


class CentralizedEconomy(Civic):
    def __init__(self, *args, **kwargs):
        super().__init__(
            key="core.culture.civics.centralized_economy",
            name=_t("content.culture.civics.core.centralized_economy.name"),
            description=_t("content.culture.civics.core.centralized_economy.description"),
            *args,
            **kwargs,
        )
