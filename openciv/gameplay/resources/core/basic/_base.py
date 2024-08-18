from __future__ import annotations
from openciv.gameplay.resource import Resource, ResourceValueType, ResourceTypeBasic


class BasicBaseResource(Resource):
    def __init__(self, *args, **kwargs):
        super().__init__(configure_as_float_or_int=ResourceValueType.FLOAT, type=ResourceTypeBasic, *args, **kwargs)
