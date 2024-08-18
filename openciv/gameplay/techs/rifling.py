from __future__ import annotations
from openciv.gameplay.tech import Tech
from openciv.engine.managers.i18n import _t


class Rifling(Tech):
    def __init__(self, *args, **kwargs):
        super().__init__(
            "core.rifling",
            _t("tech.rifling.name"),
            _t("tech.rifling.description"),
            tech_points_required=20,
            *args,
            **kwargs,
        )
