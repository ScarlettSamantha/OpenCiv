from openciv.gameplay.tech import Tech
from openciv.engine.managers.i18n import _t


class NanoTechnology(Tech):
    def __init__(self, *args, **kwargs):
        super().__init__(
            "core.nano_technology",
            _t("tech.nano_technology.name"),
            _t("tech.nano_technology.description"),
            tech_points_required=20,
            *args,
            **kwargs,
        )
