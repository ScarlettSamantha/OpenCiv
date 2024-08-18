from __future__ import annotations
from openciv.gameplay.culture import Civic
from openciv.engine.managers.i18n import _t


class EducationReform(Civic):
    def __init__(self, *args, **kwargs):
        super().__init__(
            key="core.culture.civics.education_reform",
            name=_t("content.culture.civics.core.education_reform.name"),
            description=_t("content.culture.civics.core.education_reform.description"),
            *args,
            **kwargs,
        )
