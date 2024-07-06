from openciv.gameplay.tech import Tech
from openciv.engine.managers.i18n import _t


class CombinedArms(Tech):
    def __init__(self, *args, **kwargs):
        super().__init__(
            "core.combined_arms",
            _t("tech.combined_arms.name"),
            _t("tech.combined_arms.description"),
            tech_points_required=20,
            *args,
            **kwargs,
        )
