from openciv.gameplay.culture import Civic
from openciv.engine.managers.i18n import _t


class Meritocracy(Civic):
    def __init__(self, *args, **kwargs):
        super().__init__(
            key="core.culture.civics.meritocracy",
            name=_t("content.culture.civics.core.meritocracy.name"),
            description=_t("content.culture.civics.core.meritocracy.description"),
            *args,
            **kwargs,
        )
