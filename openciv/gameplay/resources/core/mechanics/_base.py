from openciv.gameplay.resource import Resource, ResourceValueType, ResourceTypeMechanic


class MechanicBaseResource(Resource):
    def __init__(self, *args, **kwargs):
        super().__init__(configure_as_float_or_int=ResourceValueType.FLOAT, type=ResourceTypeMechanic, *args, **kwargs)
