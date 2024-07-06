from openciv.gameplay.tech import Tech
from openciv.engine.managers.i18n import _t


class IronWorking(Tech):
    def __init__(self, *args, **kwargs):
        super().__init__(
            "core.iron_working",
            _t("tech.iron_working.name"),
            _t("tech.iron_working.description"),
            tech_points_required=20,
            *args,
            **kwargs,
        )
