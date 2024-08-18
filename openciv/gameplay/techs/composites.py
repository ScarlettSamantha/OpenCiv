from __future__ import annotations
from openciv.gameplay.tech import Tech
from openciv.engine.managers.i18n import _t


class Composites(Tech):
    def __init__(self, *args, **kwargs):
        super().__init__(
            "core.composites",
            _t("tech.composites.name"),
            _t("tech.composites.description"),
            tech_points_required=20,
            *args,
            **kwargs,
        )
