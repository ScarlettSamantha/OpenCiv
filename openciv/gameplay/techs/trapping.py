from openciv.gameplay.tech import Tech
from openciv.engine.managers.i18n import _t


class Trapping(Tech):
    def __init__(self, *args, **kwargs):
        super().__init__(
            "core.trapping",
            _t("tech.trapping.name"),
            _t("tech.trapping.description"),
            tech_points_required=20,
            *args,
            **kwargs,
        )
