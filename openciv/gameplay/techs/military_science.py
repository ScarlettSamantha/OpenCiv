from openciv.gameplay.tech import Tech
from openciv.engine.managers.i18n import _t


class MilitaryScience(Tech):
    def __init__(self, *args, **kwargs):
        super().__init__(
            "core.military_science",
            _t("tech.military_science.name"),
            _t("tech.military_science.description"),
            tech_points_required=20,
            *args,
            **kwargs,
        )
