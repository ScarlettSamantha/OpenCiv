from openciv.gameplay.tech import Tech
from openciv.engine.managers.i18n import _t


class GuidanceSystems(Tech):
    def __init__(self, *args, **kwargs):
        super().__init__(
            "core.guidance_systems",
            _t("tech.guidance_systems.name"),
            _t("tech.guidance_systems.description"),
            tech_points_required=20,
            *args,
            **kwargs,
        )
