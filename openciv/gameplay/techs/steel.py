from openciv.gameplay.tech import Tech
from openciv.engine.managers.i18n import _t


class Steel(Tech):
    def __init__(self, *args, **kwargs):
        super().__init__(
            "core.steel",
            _t("tech.steel.name"),
            _t("tech.steel.description"),
            tech_points_required=20,
            *args,
            **kwargs,
        )
