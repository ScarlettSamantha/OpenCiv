from __future__ import annotations
from openciv.gameplay.tech import Tech
from openciv.engine.managers.i18n import _t


class Electricity(Tech):
    def __init__(self, *args, **kwargs):
        super().__init__(
            "core.electricity",
            _t("tech.electricity.name"),
            _t("tech.electricity.description"),
            tech_points_required=20,
            *args,
            **kwargs,
        )
