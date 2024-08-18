from __future__ import annotations
from openciv.gameplay.tech import Tech
from openciv.engine.managers.i18n import _t


class Combustion(Tech):
    def __init__(self, *args, **kwargs):
        super().__init__(
            "core.combustion",
            _t("tech.combustion.name"),
            _t("tech.combustion.description"),
            tech_points_required=20,
            *args,
            **kwargs,
        )
