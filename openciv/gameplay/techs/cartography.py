from openciv.gameplay.tech import Tech
from openciv.engine.managers.i18n import _t


class Catography(Tech):
    def __init__(self, *args, **kwargs):
        super().__init__(
            "core.cartography",
            _t("tech.cartography.name"),
            _t("tech.cartography.description"),
            tech_points_required=20,
            *args,
            **kwargs,
        )
