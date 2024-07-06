from openciv.gameplay.tech import Tech
from openciv.engine.managers.i18n import _t


class Writing(Tech):
    def __init__(self, *args, **kwargs):
        super().__init__(
            "core.writing",
            _t("tech.writing.name"),
            _t("tech.writing.description"),
            tech_points_required=20,
            *args,
            **kwargs,
        )
