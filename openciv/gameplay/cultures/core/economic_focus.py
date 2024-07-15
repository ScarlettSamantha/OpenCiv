from openciv.gameplay.culture import Civic
from openciv.engine.managers.i18n import _t


class EconomicFocus(Civic):
    def __init__(self, *args, **kwargs):
        super().__init__(
            key="core.culture.civics.economic_focus",
            name=_t("content.culture.civics.core.economic_focus.name"),
            description=_t("content.culture.civics.core.economic_focus.description"),
            *args,
            **kwargs,
        )
