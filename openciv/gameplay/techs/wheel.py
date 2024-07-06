from openciv.gameplay.tech import Tech
from openciv.engine.managers.i18n import _t


class Wheel(Tech):
    def __init__(self, *args, **kwargs):
        super().__init__(
            "core.wheel",
            _t("tech.wheel.name"),
            _t("tech.wheel.description"),
            tech_points_required=20,
            *args,
            **kwargs,
        )
