from openciv.gameplay.tech import Tech
from openciv.engine.managers.i18n import _t


class Robotics(Tech):
    def __init__(self, *args, **kwargs):
        super().__init__(
            "core.robotics",
            _t("tech.robotics.name"),
            _t("tech.robotics.description"),
            tech_points_required=20,
            *args,
            **kwargs,
        )
