from __future__ import annotations
from openciv.gameplay.culture import Civic
from openciv.engine.managers.i18n import _t


class MarketCompetition(Civic):
    def __init__(self, *args, **kwargs):
        super().__init__(
            key="core.culture.civics.market_competition",
            name=_t("content.culture.civics.core.market_competition.name"),
            description=_t("content.culture.civics.core.market_competition.description"),
            *args,
            **kwargs,
        )
