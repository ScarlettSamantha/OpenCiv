from enum import Enum
from inspect import isclass
from typing import Union, ForwardRef, List, Dict

from openciv.engine.saving import SaveAble
from openciv.engine.managers.i18n import T_TranslationOrStr, _t
from openciv.engine.exceptions.resource_exception import ResourceTypeException


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
    def __init__(self, name: T_TranslationOrStr, description: T_TranslationOrStr, _type: ResourceType):
        self._type_name: T_TranslationOrStr = name
        self._type_description: T_TranslationOrStr = description
        self._type_num: ResourceType = _type


class ResourceTypeMechanic(ResourceTypeBase):
    def __init__(self):
        super().__init__(
            _t("content.resources.core.types.mechanic.name"),
            _t("content.resources.core.types.mechanic.description"),
            ResourceType.MECHANIC,
        )


class ResourceTypeBonus(ResourceTypeBase):
    def __init__(self):
        super().__init__(
            _t("content.resources.core.types.bonus.name"),
            _t("content.resources.core.types.bonus.description"),
            ResourceType.BONUS,
        )


class ResourceTypeStrategic(ResourceTypeBase):
    def __init__(self):
        super().__init__(
            _t("content.resources.core.types.strategic.name"),
            _t("content.resources.core.types.strategic.description"),
            ResourceType.STRATEGIC,
        )


class ResourceTypeLuxury(ResourceTypeBase):
    def __init__(self):
        super().__init__(
            _t("content.resources.core.types.luxury.name"),
            _t("content.resources.core.types.luxury.description"),
            ResourceType.LUXURY,
        )


class ResourceTypeBasic(ResourceTypeBase):
    def __init__(self):
        super().__init__(
            _t("content.resources.core.types.basic.name"),
            _t("content.resources.core.types.basic.description"),
            ResourceType.BASIC,
        )


class Resource(SaveAble):
    def __init__(
        self,
        key: str,
        name: T_TranslationOrStr,
        _type: ResourceTypeBase,
        value: Union[float, int] = 0,
        configure_as_float_or_int: ResourceValueType = ResourceValueType.INT,
        icon: T_TranslationOrStr = None,
        description: T_TranslationOrStr = None,
        *args,
        **kwargs,
    ):
        super().__init__()
        self.key: str = key
        self.name: T_TranslationOrStr = name
        self.description: T_TranslationOrStr = description
        self.value: ResourceValueType = value
        self._value_storage: ResourceValueType = configure_as_float_or_int
        self._icon: T_TranslationOrStr = icon

        self._type = _type
        self._setup_saveable()

    def __add__(self, other: ForwardRef("Resource") | float | int) -> Union[float, int]:
        if isinstance(other, Resource):
            return self.value + other.value
        return self.value + other

    def __radd__(self, other: ForwardRef("Resource") | float | int) -> Union[float, int]:
        if isinstance(other, Resource):
            return other.value + self.value
        return other + self.value

    def __sub__(self, other: Union[ForwardRef("Resource"), float, int]) -> Union[float, int]:
        if isinstance(other, Resource):
            return self.value - other.value
        return self.value - other

    def __rsub__(self, other: Union[ForwardRef("Resource"), float, int]) -> Union[float, int]:
        if isinstance(other, Resource):
            return other.value - self.value
        return other - self.value

    def __mul__(self, other: Union[ForwardRef("Resource"), float, int]) -> Union[float, int]:
        if isinstance(other, Resource):
            if other.value == 0 or self.value == 0:
                return self.value
            return self.value * other.value
        return self.value * other

    def __rmul__(self, other: Union[ForwardRef("Resource"), float, int]) -> Union[float, int]:
        if isinstance(other, Resource):
            if other.value == 0 or self.value == 0:
                return self.value
            return other.value * self.value
        return other * self.value

    def __truediv__(self, other: Union[ForwardRef("Resource"), float, int]) -> float:
        if isinstance(other, Resource):
            return self.value / other.value
        return self.value / other

    def __rtruediv__(self, other: Union[ForwardRef("Resource"), float, int]) -> float:
        if isinstance(other, Resource):
            return other.value / self.value
        return other / self.value

    def __floordiv__(self, other: Union[ForwardRef("Resource"), float, int]) -> int:
        if isinstance(other, Resource):
            return self.value // other.value
        return self.value // other

    def __rfloordiv__(self, other: Union[ForwardRef("Resource"), float, int]) -> int:
        if isinstance(other, Resource):
            return other.value // self.value
        return other // self.value

    def __mod__(self, other: Union[ForwardRef("Resource"), float, int]) -> Union[float, int]:
        if isinstance(other, Resource):
            return self.value % other.value
        return self.value % other

    def __rmod__(self, other: Union[ForwardRef("Resource"), float, int]) -> Union[float, int]:
        if isinstance(other, Resource):
            return other.value % self.value
        return other % self.value

    def __pow__(self, other: Union[ForwardRef("Resource"), float, int]) -> Union[float, int]:
        if isinstance(other, Resource):
            return self.value**other.value
        return self.value**other

    def __rpow__(self, other: Union[ForwardRef("Resource"), float, int]) -> Union[float, int]:
        if isinstance(other, Resource):
            return other.value**self.value
        return other**self.value

    def __eq__(self, other: Union[ForwardRef("Resource"), float, int]) -> bool:
        if isinstance(other, Resource):
            return self.value == other.value
        return self.value == other

    def __ne__(self, other: Union[ForwardRef("Resource"), float, int]) -> bool:
        if isinstance(other, Resource):
            return self.value != other.value
        return self.value != other

    def __lt__(self, other: Union[ForwardRef("Resource"), float, int]) -> bool:
        if isinstance(other, Resource):
            return self.value < other.value
        return self.value < other

    def __le__(self, other: Union[ForwardRef("Resource"), float, int]) -> bool:
        if isinstance(other, Resource):
            return self.value <= other.value
        return self.value <= other

    def __gt__(self, other: Union[ForwardRef("Resource"), float, int]) -> bool:
        if isinstance(other, Resource):
            return self.value > other.value
        return self.value > other

    def __ge__(self, other: Union[ForwardRef("Resource"), float, int]) -> bool:
        if isinstance(other, Resource):
            return self.value >= other.value
        return self.value >= other

    def __repr__(self) -> str:
        return f"{self.key}: {self.value}"

    @classmethod
    def strategic(cls, *args, **kwargs) -> ForwardRef("Resource"):
        return cls(*args, **kwargs, _type=ResourceTypeStrategic)

    @classmethod
    def luxury(cls, *args, **kwargs) -> ForwardRef("Resource"):
        return cls(*args, **kwargs, _type=ResourceTypeLuxury)

    @classmethod
    def bonus(cls, *args, **kwargs) -> ForwardRef("Resource"):
        return cls(*args, **kwargs, _type=ResourceTypeBonus)

    @classmethod
    def basic(cls, *args, **kwargs) -> ForwardRef("Resource"):
        return cls(*args, **kwargs, _type=ResourceTypeBase)

    @classmethod
    def mechanic(cls, *args, **kwargs) -> ForwardRef("Resource"):
        return cls(*args, **kwargs, _type=ResourceTypeMechanic)


mapping = {
    ResourceType.MECHANIC: ResourceTypeMechanic,
    ResourceType.BASIC: ResourceTypeBasic,
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
