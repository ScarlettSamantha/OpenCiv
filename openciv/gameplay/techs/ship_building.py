from __future__ import annotations
from openciv.gameplay.tech import Tech
from openciv.engine.managers.i18n import _t


class ShipBuilding(Tech):
    def __init__(self, *args, **kwargs):
        super().__init__(
            "core.ship_building",
            _t("tech.ship_building.name"),
            _t("tech.ship_building.description"),
            tech_points_required=20,
            *args,
            **kwargs,
        )
