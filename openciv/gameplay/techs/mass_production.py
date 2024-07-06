from openciv.gameplay.tech import Tech
from openciv.engine.managers.i18n import _t


class MassProduction(Tech):
    def __init__(self, *args, **kwargs):
        super().__init__(
            "core.mass_production",
            _t("tech.mass_production.name"),
            _t("tech.mass_production.description"),
            tech_points_required=20,
            *args,
            **kwargs,
        )
