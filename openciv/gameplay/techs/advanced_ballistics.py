from openciv.gameplay.tech import Tech
from openciv.engine.managers.i18n import _t


class AdvancedBallistics(Tech):
    def __init__(self, *args, **kwargs):
        super().__init__(
            "core.advanced_ballistics",
            _t("tech.advanced_ballistics.name"),
            _t("tech.advanced_ballistics.description"),
            tech_points_required=20,
            *args,
            **kwargs,
        )
