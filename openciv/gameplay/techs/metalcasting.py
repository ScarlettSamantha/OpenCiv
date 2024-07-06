from openciv.gameplay.tech import Tech
from openciv.engine.managers.i18n import _t


class MetalCasting(Tech):
    def __init__(self, *args, **kwargs):
        super().__init__(
            "core.metal_casting",
            _t("tech.metal_casting.name"),
            _t("tech.metal_casting.description"),
            tech_points_required=20,
            *args,
            **kwargs,
        )
