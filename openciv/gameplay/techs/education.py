from openciv.gameplay.tech import Tech
from openciv.engine.managers.i18n import _t


class Education(Tech):
    def __init__(self, *args, **kwargs):
        super().__init__(
            "core.education",
            _t("tech.education.name"),
            _t("tech.education.description"),
            tech_points_required=20,
            *args,
            **kwargs,
        )
