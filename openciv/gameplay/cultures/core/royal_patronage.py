from __future__ import annotations
from openciv.gameplay.culture import Civic
from openciv.engine.managers.i18n import _t


class RoyalPatronage(Civic):
    def __init__(self, *args, **kwargs):
        super().__init__(
            key="core.culture.civics.royal_patronage",
            name=_t("content.culture.civics.core.royal_patronage.name"),
            description=_t("content.culture.civics.core.royal_patronage.description"),
            *args,
            **kwargs,
        )
