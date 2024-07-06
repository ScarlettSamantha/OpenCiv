from openciv.gameplay.tech import Tech
from openciv.engine.managers.i18n import _t


class HuntingGethering(Tech):
    def __init__(self, *args, **kwargs):
        super().__init__(
            "core.hunting_gethering",
            _t("tech.hunting_gethering.name"),
            _t("tech.hunting_gethering.description"),
            tech_points_required=20,
            *args,
            **kwargs,
        )
