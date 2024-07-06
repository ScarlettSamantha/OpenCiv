from openciv.gameplay.tech import Tech
from openciv.engine.managers.i18n import _t


class SteamPower(Tech):
    def __init__(self, *args, **kwargs):
        super().__init__(
            "core.steam_power",
            _t("tech.steam_power.name"),
            _t("tech.steam_power.description"),
            tech_points_required=20,
            *args,
            **kwargs,
        )
