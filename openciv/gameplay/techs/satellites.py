from openciv.gameplay.tech import Tech
from openciv.engine.managers.i18n import _t


class Satellites(Tech):
    def __init__(self, *args, **kwargs):
        super().__init__(
            "core.satellites",
            _t("tech.satellites.name"),
            _t("tech.satellites.description"),
            tech_points_required=20,
            *args,
            **kwargs,
        )
