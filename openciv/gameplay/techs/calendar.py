from __future__ import annotations
from openciv.gameplay.tech import Tech
from openciv.engine.managers.i18n import _t


class Calendar(Tech):
    def __init__(self, *args, **kwargs):
        super().__init__(
            "core.calendar",
            _t("tech.calendar.name"),
            _t("tech.calendar.description"),
            tech_points_required=20,
            *args,
            **kwargs,
        )
