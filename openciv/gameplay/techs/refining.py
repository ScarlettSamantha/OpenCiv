from openciv.gameplay.tech import Tech
from openciv.engine.managers.i18n import _t


class Refining(Tech):
    def __init__(self, *args, **kwargs):
        super().__init__(
            "core.refining",
            _t("tech.refining.name"),
            _t("tech.refining.description"),
            tech_points_required=20,
            *args,
            **kwargs,
        )
