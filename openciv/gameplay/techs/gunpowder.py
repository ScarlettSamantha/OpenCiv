from __future__ import annotations
from openciv.gameplay.tech import Tech
from openciv.engine.managers.i18n import _t


class Gunpowder(Tech):
    def __init__(self, *args, **kwargs):
        super().__init__(
            "core.gunpowder",
            _t("tech.gunpowder.name"),
            _t("tech.gunpowder.description"),
            tech_points_required=20,
            *args,
            **kwargs,
        )
