from openciv.gameplay.resource import Resource, ResourceTypeLuxury, ResourceValueType

from openciv.engine.managers.i18n import _t


class Dogs(Resource):
    def __init__(self, value: int = 0):
        super().__init__(
            "core.bonus.dogs",
            _t("content.resources.core.dogs"),
            value,
            ResourceTypeLuxury,
            ResourceValueType.INT,
        )
