from openciv.gameplay.culture import Civic
from openciv.engine.managers.i18n import _t


class FaithBasedEducation(Civic):
    def __init__(self, *args, **kwargs):
        super().__init__(
            key="core.culture.civics.faith_based_education",
            name=_t("content.culture.civics.core.faith_based_education.name"),
            description=_t("content.culture.civics.core.faith_based_education.description"),
            *args,
            **kwargs,
        )
