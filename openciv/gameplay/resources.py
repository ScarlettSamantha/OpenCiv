from openciv.gameplay.resource import (
    ResourceType,
    Resource,
    ResourceTypeBase,
    ResourceTypeBonus,
    ResourceTypeLuxury,
    ResourceTypeStrategic,
)
from typing import Dict, Union, List
from openciv.engine.exceptions.resource_exception import ResourceTypeException
from inspect import isclass

mapping = {
    ResourceType.BONUS: ResourceTypeBonus,
    ResourceType.STRATEGIC: ResourceTypeStrategic,
    ResourceType.LUXURY: ResourceTypeLuxury,
}


class Resources:
    def __init__(self):
        self.resources: Dict[ResourceTypeBase, Dict[str, Resource]] = {}
        self.define_types()

    def define_types(self) -> None:
        global mapping

        self.resources = {}
        for resource_type in ResourceType:
            self.resources[mapping[resource_type]] = {}

    def get(
        self, _type: ResourceType = None, key: str = None
    ) -> Dict[str, Resource] | Dict[str, Dict[str, Resource]] | Resource:
        if _type:
            if key and _type in self.resources:
                if key in self.resources[_type]:
                    return self.resources[_type][key]
                else:
                    raise KeyError(f"Key {key} not found in resources")
            else:
                raise KeyError(f"Key {key} not found in resources")
            return self.resources[_type]
        return self.resources

    def toDict(self):
        return self.resources

    def add(self, resource: Union[Resource | List], auto_instance: bool = True) -> None:
        def _add(self, _resource: Resource):
            resource_type_class = _resource._type

            if resource_type_class not in self.resources:
                self.resources[resource_type_class] = {}
            if auto_instance and isclass(_resource):
                _resource = _resource()
            self.resources[resource_type_class][_resource.key] = _resource

        _add(self, resource) if isinstance(resource, Resource) else [_add(self, r) for r in resource]

    def __add__(self, b: Resource) -> None:
        if not isinstance(b, Resource):
            raise ResourceTypeException("Can only add resource to resources")
        if b._type is None:
            raise ResourceTypeException("Resource must have a type")
        self.add(b)

    def __getitem__(self, key) -> Dict[str, Resource] | Resource:
        if isinstance(key, ResourceType):
            return self.get(key)
        if isinstance(key, str) and "." in key:
            key = key.split(".")
            return self.get(ResourceType[key[0]], key[1])
        return self.get(ResourceType[key])

    def __setitem__(self, key, value) -> None:
        self.add(value)
