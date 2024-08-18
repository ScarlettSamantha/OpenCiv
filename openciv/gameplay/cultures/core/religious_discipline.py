from __future__ import annotations
from openciv.gameplay.culture import Civic
from openciv.engine.managers.i18n import _t


class ReligiousDiscipline(Civic):
    def __init__(self, *args, **kwargs):
        super().__init__(
            key="core.culture.civics.religious_discipline",
            name=_t("content.culture.civics.core.religious_discipline.name"),
            description=_t("content.culture.civics.core.religious_discipline.description"),
            *args,
            **kwargs,
        )
