from openciv.gameplay.tech import Tech
from openciv.engine.managers.i18n import _t


class Lasers(Tech):
    def __init__(self, *args, **kwargs):
        super().__init__(
            "core.lasers",
            _t("tech.lasers.name"),
            _t("tech.lasers.description"),
            tech_points_required=20,
            *args,
            **kwargs,
        )
