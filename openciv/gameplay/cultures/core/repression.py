from openciv.gameplay.culture import Civic
from openciv.engine.managers.i18n import _t


class Repression(Civic):
    def __init__(self, *args, **kwargs):
        super().__init__(
            key="core.culture.civics.repression",
            name=_t("content.culture.civics.core.repression.name"),
            description=_t("content.culture.civics.core.repression.description"),
            *args,
            **kwargs,
        )
