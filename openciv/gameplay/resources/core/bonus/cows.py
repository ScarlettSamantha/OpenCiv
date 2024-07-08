from openciv.gameplay.resource import Resource, ResourceTypeBonus, ResourceValueType

from openciv.engine.managers.i18n import _t


class Cows(Resource):
    def __init__(self, value: int = 0):
        super().__init__(
            "core.bonus.cows",
            _t("content.resources.core.cows"),
            value,
            ResourceTypeBonus,
            ResourceValueType.INT,
        )
