from openciv.gameplay.culture import Civic
from openciv.engine.managers.i18n import _t


class TotalitarianControl(Civic):
    def __init__(self, *args, **kwargs):
        super().__init__(
            key="core.culture.civics.totalitarian_control",
            name=_t("content.culture.civics.core.totalitarian_control.name"),
            description=_t("content.culture.civics.core.totalitarian_control.description"),
            *args,
            **kwargs,
        )
