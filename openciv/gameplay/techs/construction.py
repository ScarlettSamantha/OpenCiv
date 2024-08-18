from __future__ import annotations
from openciv.gameplay.tech import Tech
from openciv.engine.managers.i18n import _t


class Construction(Tech):
    def __init__(self, *args, **kwargs):
        super().__init__(
            "core.construction",
            _t("tech.construction.name"),
            _t("tech.construction.description"),
            tech_points_required=20,
            *args,
            **kwargs,
        )
