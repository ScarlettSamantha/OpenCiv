from openciv.gameplay.tech import Tech
from openciv.engine.managers.i18n import _t


class Chemistry(Tech):
    def __init__(self, *args, **kwargs):
        super().__init__(
            "core.chemistry",
            _t("tech.chemistry.name"),
            _t("tech.chemistry.description"),
            tech_points_required=20,
            *args,
            **kwargs,
        )
