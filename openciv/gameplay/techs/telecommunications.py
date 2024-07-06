from openciv.gameplay.tech import Tech
from openciv.engine.managers.i18n import _t


class Telecommunications(Tech):
    def __init__(self, *args, **kwargs):
        super().__init__(
            "core.telecommunications",
            _t("tech.telecommunications.name"),
            _t("tech.telecommunications.description"),
            tech_points_required=20,
            *args,
            **kwargs,
        )
