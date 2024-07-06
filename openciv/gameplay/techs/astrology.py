from openciv.gameplay.tech import Tech
from openciv.engine.managers.i18n import _t


class Astrology(Tech):
    def __init__(self, *args, **kwargs):
        super().__init__(
            "core.astrology",
            _t("tech.astrology.name"),
            _t("tech.astrology.description"),
            tech_points_required=20,
            *args,
            **kwargs,
        )
