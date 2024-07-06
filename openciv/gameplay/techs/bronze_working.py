from openciv.gameplay.tech import Tech
from openciv.engine.managers.i18n import _t


class BronzeWorking(Tech):
    def __init__(self, *args, **kwargs):
        super().__init__(
            "core.bronze_working",
            _t("tech.bronze_working.name"),
            _t("tech.bronze_working.description"),
            tech_points_required=20,
            *args,
            **kwargs,
        )
