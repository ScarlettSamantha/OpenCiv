from __future__ import annotations
from openciv.gameplay.resource import Resource, ResourceTypeStrategic, ResourceValueType

from openciv.engine.managers.i18n import _t


class Horses(Resource):
    def __init__(self, value: int = 0):
        super().__init__(
            "core.strategic.horses",
            _t("content.resources.core.horses"),
            value,
            ResourceTypeStrategic,
            ResourceValueType.INT,
        )
