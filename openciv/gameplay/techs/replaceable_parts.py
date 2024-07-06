from openciv.gameplay.tech import Tech
from openciv.engine.managers.i18n import _t


class ReplacableParts(Tech):
    def __init__(self, *args, **kwargs):
        super().__init__(
            "core.replcable_parts",
            _t("tech.replcable_parts.name"),
            _t("tech.replcable_parts.description"),
            tech_points_required=20,
            *args,
            **kwargs,
        )
