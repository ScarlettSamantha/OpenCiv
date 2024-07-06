from openciv.gameplay.tech import Tech
from openciv.engine.managers.i18n import _t


class Ballistics(Tech):
    def __init__(self, *args, **kwargs):
        super().__init__(
            "core.ballistics",
            _t("tech.ballistics.name"),
            _t("tech.ballistics.description"),
            tech_points_required=20,
            *args,
            **kwargs,
        )
