from openciv.gameplay.tech import Tech
from openciv.engine.managers.i18n import _t


class Astronomy(Tech):
    def __init__(self, *args, **kwargs):
        super().__init__(
            "core.astronomy",
            _t("tech.astronomy.name"),
            _t("tech.astronomy.description"),
            tech_points_required=20,
            *args,
            **kwargs,
        )
