from __future__ import annotations

from enum import Enum
from typing import Union, List, Dict, Any, Self, Type

from openciv.engine.saving import SaveAble
from openciv.engine.managers.i18n import T_TranslationOrStr, t_


class ResourceType(Enum):
    MECHANIC = -1
    BASIC = 0
    BONUS = 1
    STRATEGIC = 2
    LUXURY = 3


class ResourceValueType(Enum):
    FLOAT = 0
    INT = 1


class ResourceTypeBase:
    def __init__(self, name: T_TranslationOrStr, description: T_TranslationOrStr, type_: ResourceType):
        self.type_name: T_TranslationOrStr = name
        self.type_description: T_TranslationOrStr = description
        self.type_num: ResourceType = type_


class ResourceTypeMechanic(ResourceTypeBase):
    def __init__(self):
        super().__init__(
            t_("content.resources.core.types.mechanic.name"),
            t_("content.resources.core.types.mechanic.description"),
            ResourceType.MECHANIC,
        )


class ResourceTypeBonus(ResourceTypeBase):
    def __init__(self):
        super().__init__(
            t_("content.resources.core.types.bonus.name"),
            t_("content.resources.core.types.bonus.description"),
            ResourceType.BONUS,
        )


class ResourceTypeStrategic(ResourceTypeBase):
    def __init__(self):
        super().__init__(
            t_("content.resources.core.types.strategic.name"),
            t_("content.resources.core.types.strategic.description"),
            ResourceType.STRATEGIC,
        )


class ResourceTypeLuxury(ResourceTypeBase):
    def __init__(self):
        super().__init__(
            t_("content.resources.core.types.luxury.name"),
            t_("content.resources.core.types.luxury.description"),
            ResourceType.LUXURY,
        )


class ResourceTypeBasic(ResourceTypeBase):
    def __init__(self):
        super().__init__(
            t_("content.resources.core.types.basic.name"),
            t_("content.resources.core.types.basic.description"),
            ResourceType.BASIC,
        )


class Resource(SaveAble):
    def __init__(
        self,
        key: str,
        name: T_TranslationOrStr,
        type_: Type[ResourceTypeBase],
        value: Union[float, int] = 0,
        configure_as_float_or_int: ResourceValueType = ResourceValueType.INT,
        icon: T_TranslationOrStr | None = None,
        description: T_TranslationOrStr | None = None,
        *args: Any,
        **kwargs: Any,
    ):
        super().__init__()
        self.key: str = key
        self.name: T_TranslationOrStr = name
        self.description: T_TranslationOrStr | None = description
        self.value: Union[float, int] = value
        self.value_storage: ResourceValueType = configure_as_float_or_int
        self.icon: T_TranslationOrStr | None = icon

        self.type = type_
        self._setup_saveable()

    # Overloaded operators
    def __add__(self, other: Union[Resource, float, int]) -> Union[float, int]:
        if isinstance(other, Resource):
            return self.value + other.value
        return self.value + other

    def __radd__(self, other: Union[Resource, float, int]) -> Union[float, int]:
        return self.__add__(other)

    def __sub__(self, other: Union[Resource, float, int]) -> Union[float, int]:
        if isinstance(other, Resource):
            return self.value - other.value
        return self.value - other

    def __rsub__(self, other: Union[Resource, float, int]) -> Union[float, int]:
        if isinstance(other, Resource):
            return other.value - self.value
        return other - self.value

    def __mul__(self, other: Union[Resource, float, int]) -> Union[float, int]:
        if isinstance(other, Resource):
            return self.value * other.value
        return self.value * other

    def __rmul__(self, other: Union[Resource, float, int]) -> Union[float, int]:
        return self.__mul__(other)

    def __truediv__(self, other: Union[Resource, float, int]) -> float:
        if isinstance(other, Resource):
            return self.value / other.value
        return self.value / other

    def __rtruediv__(self, other: Union[Resource, float, int]) -> float:
        if isinstance(other, Resource):
            return other.value / self.value
        return other / self.value

    def __floordiv__(self, other: Union[Resource, float, int]) -> int:
        if isinstance(other, Resource):
            return int(self.value // other.value)
        return int(self.value // other)

    def __rfloordiv__(self, other: Union[Resource, float, int]) -> int:
        return self.__floordiv__(other)

    def __mod__(self, other: Union[Resource, float, int]) -> Union[float, int]:
        if isinstance(other, Resource):
            return self.value % other.value
        return self.value % other

    def __rmod__(self, other: Union[Resource, float, int]) -> Union[float, int]:
        return self.__mod__(other)

    def __pow__(self, other: Union[Resource, float, int]) -> Union[float, int]:
        if isinstance(other, Resource):
            return self.value**other.value
        return self.value**other

    def __rpow__(self, other: Union[Resource, float, int]) -> Union[float, int]:
        return self.__pow__(other)

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Resource):
            return self.value == other.value
        return False

    def __ne__(self, other: object) -> bool:
        return not self.__eq__(other)

    def __lt__(self, other: Union[Resource, float, int]) -> bool:
        if isinstance(other, Resource):
            return self.value < other.value
        return self.value < other

    def __le__(self, other: Union[Resource, float, int]) -> bool:
        if isinstance(other, Resource):
            return self.value <= other.value
        return self.value <= other

    def __gt__(self, other: Union[Resource, float, int]) -> bool:
        if isinstance(other, Resource):
            return self.value > other.value
        return self.value > other

    def __ge__(self, other: Union[Resource, float, int]) -> bool:
        if isinstance(other, Resource):
            return self.value >= other.value
        return self.value >= other

    def __repr__(self) -> str:
        return f"{self.key}: {self.value}"

    @classmethod
    def strategic(cls, *args: Any, **kwargs: Any) -> Resource:
        return cls(*args, **kwargs, type_=ResourceTypeStrategic)

    @classmethod
    def luxury(cls, *args: Any, **kwargs: Any) -> Resource:
        return cls(*args, **kwargs, type_=ResourceTypeLuxury)

    @classmethod
    def bonus(cls, *args: Any, **kwargs: Any) -> Resource:
        return cls(*args, **kwargs, type_=ResourceTypeBonus)

    @classmethod
    def basic(cls, *args: Any, **kwargs: Any) -> Resource:
        return cls(*args, **kwargs, type_=ResourceTypeBasic)

    @classmethod
    def mechanic(cls, *args: Any, **kwargs: Any) -> Resource:
        return cls(*args, **kwargs, type_=ResourceTypeMechanic)


mapping: Dict[ResourceType, Type[ResourceTypeBase]] = {
    ResourceType.MECHANIC: ResourceTypeMechanic,
    ResourceType.BASIC: ResourceTypeBasic,
    ResourceType.BONUS: ResourceTypeBonus,
    ResourceType.STRATEGIC: ResourceTypeStrategic,
    ResourceType.LUXURY: ResourceTypeLuxury,
}


class Resources:
    def __init__(self):
        self.resources: Dict[Type[ResourceTypeBase], Dict[str, Resource]] = {}
        self.define_types()

    def define_types(self) -> None:
        global mapping
        for item in mapping.values():
            if item not in self.resources.keys():
                self.resources[item] = {}

    def flatten(self) -> Dict[str, Resource]:
        return {key: resource for sub_dict in self.resources.values() for key, resource in sub_dict.items()}

    def get(
        self, _type: Type[ResourceTypeBase] | None = None, key: str | None = None
    ) -> Dict[Type[ResourceTypeBase], Dict[str, Resource]] | Resource | Dict[str, Resource]:
        if _type is None:
            for sub_dict in self.resources.values():
                for resource in sub_dict.values():
                    if resource.key == key:
                        return resource
                raise KeyError(f"Key {key} not found in resources")
        else:
            sub: Dict[str, Resource] = self.resources[_type]
            if key is not None:
                if key not in sub:
                    raise KeyError(f"Key {key} not found in resources")
                return sub[key]
        return self.resources

    def toDict(self) -> Dict[Type[ResourceTypeBase], Dict[str, Resource]]:
        return self.resources

    def add(self, resource: Union[Resource, List[Resource]], auto_instance: bool = True) -> None:
        def _add(self: Self, tmp_resource: Resource) -> None:
            resource_type: Type[ResourceTypeBase] = tmp_resource.type
            if resource_type not in self.resources:
                self.resources[resource_type] = {}
            self.resources[resource_type][tmp_resource.key] = tmp_resource

        if isinstance(resource, Resource):
            _add(self=self, tmp_resource=resource)
        else:
            for r in resource:
                _add(self=self, tmp_resource=r)

    def __add__(self, b: Resource) -> None:
        self.add(b)

    def __getitem__(self, key: str) -> Dict[str, Resource] | Resource:
        return self.flatten()[key]


class Costs:
    def __init__(self, costs: List[Resource] | Resource) -> None:
        self.costs: List[Resource] = costs if isinstance(costs, list) else [costs]
