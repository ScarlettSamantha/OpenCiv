from __future__ import annotations
from openciv.gameplay.tech import Tech
from openciv.engine.managers.i18n import _t


class Computers(Tech):
    def __init__(self, *args, **kwargs):
        super().__init__(
            "core.computers",
            _t("tech.computers.name"),
            _t("tech.computers.description"),
            tech_points_required=20,
            *args,
            **kwargs,
        )
