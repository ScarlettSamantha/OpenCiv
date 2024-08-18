from __future__ import annotations
from openciv.gameplay.resource import Resource, ResourceTypeLuxury, ResourceValueType

from openciv.engine.managers.i18n import _t


class Ivory(Resource):
    def __init__(self, value: int = 0):
        super().__init__(
            "core.bonus.ivory",
            _t("content.resources.core.ivory"),
            value,
            ResourceTypeLuxury,
            ResourceValueType.INT,
        )
