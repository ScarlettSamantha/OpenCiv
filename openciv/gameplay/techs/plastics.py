from openciv.gameplay.tech import Tech
from openciv.engine.managers.i18n import _t


class Plastics(Tech):
    def __init__(self, *args, **kwargs):
        super().__init__(
            "core.plastics",
            _t("tech.plastics.name"),
            _t("tech.plastics.description"),
            tech_points_required=20,
            *args,
            **kwargs,
        )
