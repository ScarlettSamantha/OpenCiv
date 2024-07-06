from openciv.gameplay.tech import Tech
from openciv.engine.managers.i18n import _t


class Butress(Tech):
    def __init__(self, *args, **kwargs):
        super().__init__(
            "core.butress",
            _t("tech.butress.name"),
            _t("tech.butress.description"),
            tech_points_required=20,
            *args,
            **kwargs,
        )
