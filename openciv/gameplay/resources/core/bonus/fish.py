from openciv.gameplay.resource import Resource, ResourceTypeBonus, ResourceValueType

from openciv.engine.managers.i18n import _t


class Fish(Resource):
    def __init__(self, value: int = 0):
        super().__init__(
            "core.bonus.fish",
            _t("content.resources.core.fish"),
            value,
            ResourceTypeBonus,
            ResourceValueType.INT,
        )
