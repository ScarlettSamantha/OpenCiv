from openciv.gameplay.culture import Civic
from openciv.engine.managers.i18n import _t


class Oppression(Civic):
    def __init__(self, *args, **kwargs):
        super().__init__(
            key="core.culture.civics.oppression",
            name=_t("content.culture.civics.core.oppression.name"),
            description=_t("content.culture.civics.core.oppression.description"),
            *args,
            **kwargs,
        )
