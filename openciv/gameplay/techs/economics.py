from openciv.gameplay.tech import Tech
from openciv.engine.managers.i18n import _t


class Economics(Tech):
    def __init__(self, *args, **kwargs):
        super().__init__(
            "core.economics",
            _t("tech.economics.name"),
            _t("tech.economics.description"),
            tech_points_required=20,
            *args,
            **kwargs,
        )
