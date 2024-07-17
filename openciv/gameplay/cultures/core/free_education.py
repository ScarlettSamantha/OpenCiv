from openciv.gameplay.culture import Civic
from openciv.engine.managers.i18n import _t


class FreeEducation(Civic):
    def __init__(self, *args, **kwargs):
        super().__init__(
            key="core.culture.civics.free_education",
            name=_t("content.culture.civics.core.free_education.name"),
            description=_t("content.culture.civics.core.free_education.description"),
            *args,
            **kwargs,
        )
