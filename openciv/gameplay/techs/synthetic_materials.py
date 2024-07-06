from openciv.gameplay.tech import Tech
from openciv.engine.managers.i18n import _t


class SyntheticMaterials(Tech):
    def __init__(self, *args, **kwargs):
        super().__init__(
            "core.synthetic_materials",
            _t("tech.synthetic_materials.name"),
            _t("tech.synthetic_materials.description"),
            tech_points_required=20,
            *args,
            **kwargs,
        )
