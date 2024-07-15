from openciv.gameplay.culture import Civic
from openciv.engine.managers.i18n import _t


class LobbyingPower(Civic):
    def __init__(self, *args, **kwargs):
        super().__init__(
            key="core.culture.civics.lobbying_power",
            name=_t("content.culture.civics.core.lobbying_power.name"),
            description=_t("content.culture.civics.core.lobbying_power.description"),
            *args,
            **kwargs,
        )
