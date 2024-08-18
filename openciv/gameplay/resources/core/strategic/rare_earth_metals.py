from __future__ import annotations
from openciv.gameplay.resource import Resource, ResourceTypeStrategic, ResourceValueType

from openciv.engine.managers.i18n import _t


class RareEarthMetals(Resource):
    def __init__(self, value: int = 0):
        super().__init__(
            "core.strategic.rare_earth_metals",
            _t("content.resources.core.rare_earth_metals"),
            value,
            ResourceTypeStrategic,
            ResourceValueType.INT,
        )
