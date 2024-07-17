from openciv.gameplay.culture import Civic
from openciv.engine.managers.i18n import _t


class InnovationFocus(Civic):
    def __init__(self, *args, **kwargs):
        super().__init__(
            key="core.culture.civics.innovation_focus",
            name=_t("content.culture.civics.core.innovation_focus.name"),
            description=_t("content.culture.civics.core.innovation_focus.description"),
            *args,
            **kwargs,
        )
