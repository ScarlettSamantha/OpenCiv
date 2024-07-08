from openciv.gameplay.resource import Resource, ResourceTypeBonus, ResourceValueType

from openciv.engine.managers.i18n import _t


class Hardwood(Resource):
    def __init__(self, value: int = 0):
        super().__init__(
            "core.bonus.hardwood",
            _t("content.resources.core.hardwood"),
            value,
            ResourceTypeBonus,
            ResourceValueType.INT,
        )
