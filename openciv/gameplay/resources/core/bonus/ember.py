from openciv.gameplay.resource import Resource, ResourceTypeBonus, ResourceValueType

from openciv.engine.managers.i18n import _t


class Ember(Resource):
    def __init__(self, value: int = 0):
        super().__init__(
            "core.bonus.ember",
            _t("content.resources.core.ember"),
            value,
            ResourceTypeBonus,
            ResourceValueType.INT,
        )
