from openciv.gameplay.resource import Resource, ResourceTypeStrategic, ResourceValueType

from openciv.engine.managers.i18n import _t


class Gas(Resource):
    def __init__(self, value: int = 0):
        super().__init__(
            "core.strategic.gas",
            _t("content.resources.core.gas"),
            value,
            ResourceTypeStrategic,
            ResourceValueType.INT,
        )
