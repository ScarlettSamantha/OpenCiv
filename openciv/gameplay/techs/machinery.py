from openciv.gameplay.tech import Tech
from openciv.engine.managers.i18n import _t


class Machinery(Tech):
    def __init__(self, *args, **kwargs):
        super().__init__(
            "core.machinery",
            _t("tech.machinery.name"),
            _t("tech.machinery.description"),
            tech_points_required=20,
            *args,
            **kwargs,
        )
