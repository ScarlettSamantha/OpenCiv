from __future__ import annotations
from openciv.gameplay.tech import Tech
from openciv.engine.managers.i18n import _t


class NuclearFusion(Tech):
    def __init__(self, *args, **kwargs):
        super().__init__(
            "core.nuclear_fusion",
            _t("tech.nuclear_fusion.name"),
            _t("tech.nuclear_fusion.description"),
            tech_points_required=20,
            *args,
            **kwargs,
        )
