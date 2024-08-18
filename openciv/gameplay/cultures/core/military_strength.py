from __future__ import annotations
from openciv.gameplay.culture import Civic
from openciv.engine.managers.i18n import _t


class MilitaryStrength(Civic):
    def __init__(self, *args, **kwargs):
        super().__init__(
            key="core.culture.civics.military_strength",
            name=_t("content.culture.civics.core.military_strength.name"),
            description=_t("content.culture.civics.core.military_strength.description"),
            *args,
            **kwargs,
        )
