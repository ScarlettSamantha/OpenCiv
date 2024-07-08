from openciv.gameplay.resource import Resource, ResourceTypeBonus, ResourceValueType

from openciv.engine.managers.i18n import _t


class Copper(Resource):
    def __init__(self, value: int = 0):
        super().__init__(
            "core.bonus.copper",
            _t("content.resources.core.copper"),
            value,
            ResourceTypeBonus,
            ResourceValueType.INT,
        )
