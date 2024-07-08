from openciv.gameplay.resource import Resource, ResourceTypeLuxury, ResourceValueType

from openciv.engine.managers.i18n import _t


class Silver(Resource):
    def __init__(self, value: int = 0):
        super().__init__(
            "core.luxury.silver",
            _t("content.resources.core.silver"),
            value,
            ResourceTypeLuxury,
            ResourceValueType.INT,
        )
