from openciv.gameplay.tech import Tech
from openciv.engine.managers.i18n import _t


class CelestialNavigation(Tech):
    def __init__(self, *args, **kwargs):
        super().__init__(
            "core.celestial_navigation",
            _t("tech.celestial_navigation.name"),
            _t("tech.celestial_navigation.description"),
            tech_points_required=20,
            *args,
            **kwargs,
        )
