from openciv.gameplay.tech import Tech
from openciv.engine.managers.i18n import _t


class Sailing(Tech):
    def __init__(self, *args, **kwargs):
        super().__init__(
            "core.sailing",
            _t("tech.saling.name"),
            _t("tech.saling.description"),
            tech_points_required=20,
            *args,
            **kwargs,
        )
