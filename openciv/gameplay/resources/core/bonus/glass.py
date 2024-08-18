from __future__ import annotations
from openciv.gameplay.resource import Resource, ResourceTypeBonus, ResourceValueType

from openciv.engine.managers.i18n import _t


class Glass(Resource):
    def __init__(self, value: int = 0):
        super().__init__(
            "core.bonus.glass",
            _t("content.resources.core.glass"),
            value,
            ResourceTypeBonus,
            ResourceValueType.INT,
        )
