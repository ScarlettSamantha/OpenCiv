from openciv.gameplay.culture import Civic
from openciv.engine.managers.i18n import _t


class NobilitySystem(Civic):
    def __init__(self, *args, **kwargs):
        super().__init__(
            key="core.culture.civics.nobility_system",
            name=_t("content.culture.civics.core.nobility_system.name"),
            description=_t("content.culture.civics.core.nobility_system.description"),
            *args,
            **kwargs,
        )
