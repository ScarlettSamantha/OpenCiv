from openciv.gameplay.culture import Civic
from openciv.engine.managers.i18n import _t


class MoralPolicing(Civic):
    def __init__(self, *args, **kwargs):
        super().__init__(
            key="core.culture.civics.moral_policing",
            name=_t("content.culture.civics.core.moral_policing.name"),
            description=_t("content.culture.civics.core.moral_policing.description"),
            *args,
            **kwargs,
        )
