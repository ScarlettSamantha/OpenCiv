from openciv.gameplay.culture import Civic
from openciv.engine.managers.i18n import _t


class Censorship(Civic):
    def __init__(self, *args, **kwargs):
        super().__init__(
            key="core.culture.civics.censorship",
            name=_t("content.culture.civics.core.censorship.name"),
            description=_t("content.culture.civics.core.censorship.description"),
            *args,
            **kwargs,
        )
