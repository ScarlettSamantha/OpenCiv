from __future__ import annotations
from openciv.gameplay.tech import Tech
from openciv.engine.managers.i18n import _t


class Mining(Tech):
    def __init__(self, *args, **kwargs):
        super().__init__(
            "core.mining",
            _t("tech.mining.name"),
            _t("tech.mining.description"),
            tech_points_required=20,
            *args,
            **kwargs,
        )
