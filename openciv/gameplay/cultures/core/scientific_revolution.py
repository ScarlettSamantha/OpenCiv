from openciv.gameplay.culture import Civic
from openciv.engine.managers.i18n import _t


class ScientificRevolution(Civic):
    def __init__(self, *args, **kwargs):
        super().__init__(
            key="core.culture.civics.scientific_revolution",
            name=_t("content.culture.civics.core.scientific_revolution.name"),
            description=_t("content.culture.civics.core.scientific_revolution.description"),
            *args,
            **kwargs,
        )
