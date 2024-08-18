from __future__ import annotations
from openciv.gameplay.culture import Civic
from openciv.engine.managers.i18n import _t


class WealthAccumulation(Civic):
    def __init__(self, *args, **kwargs):
        super().__init__(
            key="core.culture.civics.wealth_accumulation",
            name=_t("content.culture.civics.core.wealth_accumulation.name"),
            description=_t("content.culture.civics.core.wealth_accumulation.description"),
            *args,
            **kwargs,
        )
