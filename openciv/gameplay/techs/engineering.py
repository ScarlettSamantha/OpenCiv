from openciv.gameplay.tech import Tech
from openciv.engine.managers.i18n import _t


class Engineering(Tech):
    def __init__(self, *args, **kwargs):
        super().__init__(
            "core.engineering",
            _t("tech.engineering.name"),
            _t("tech.engineering.description"),
            tech_points_required=20,
            *args,
            **kwargs,
        )
