from openciv.gameplay.tech import Tech
from openciv.engine.managers.i18n import _t


class Pottery(Tech):
    def __init__(self, *args, **kwargs):
        super().__init__(
            "core.pottery",
            _t("tech.pottery.name"),
            _t("tech.pottery.description"),
            tech_points_required=20,
            *args,
            **kwargs,
        )
