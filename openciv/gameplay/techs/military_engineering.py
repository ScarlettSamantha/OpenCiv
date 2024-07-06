from openciv.gameplay.tech import Tech
from openciv.engine.managers.i18n import _t


class MilitaryEngineering(Tech):
    def __init__(self, *args, **kwargs):
        super().__init__(
            "core.military_engineering",
            _t("tech.military_engineering.name"),
            _t("tech.military_engineering.description"),
            tech_points_required=20,
            *args,
            **kwargs,
        )
