from __future__ import annotations
from openciv.gameplay.culture import Civic
from openciv.engine.managers.i18n import _t


class Militarization(Civic):
    def __init__(self, *args, **kwargs):
        super().__init__(
            key="core.culture.civics.militarization",
            name=_t("content.culture.civics.core.militarization.name"),
            description=_t("content.culture.civics.core.militarization.description"),
            *args,
            **kwargs,
        )
