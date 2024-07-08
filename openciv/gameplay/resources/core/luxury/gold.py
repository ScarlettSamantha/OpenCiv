from openciv.gameplay.resource import Resource, ResourceTypeLuxury, ResourceValueType

from openciv.engine.managers.i18n import _t


class Gold(Resource):
    def __init__(self, value: int = 0):
        super().__init__(
            "core.luxury.gold",
            _t("content.resources.core.gold"),
            value,
            ResourceTypeLuxury,
            ResourceValueType.INT,
        )
