from __future__ import annotations
from openciv.gameplay.culture import Civic
from openciv.engine.managers.i18n import _t


class SimplifiedLiving(Civic):
    def __init__(self, *args, **kwargs):
        super().__init__(
            key="core.culture.civics.simplified_living",
            name=_t("content.culture.civics.core.simplified_living.name"),
            description=_t("content.culture.civics.core.simplified_living.description"),
            *args,
            **kwargs,
        )
