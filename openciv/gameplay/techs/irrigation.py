from __future__ import annotations
from openciv.gameplay.tech import Tech
from openciv.engine.managers.i18n import _t


class Irrigation(Tech):
    def __init__(self, *args, **kwargs):
        super().__init__(
            "core.irrigation",
            _t("tech.irrigation.name"),
            _t("tech.irrigation.description"),
            tech_points_required=20,
            *args,
            **kwargs,
        )
