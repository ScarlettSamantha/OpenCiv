from enum import Enum
from openciv.engine.managers.i18n import T_TranslationOrStr, _t
from typing import Union


class ResourceType(Enum):
    BONUS = 0
    STRATEGIC = 1
    LUXURY = 2


class ResourceValueType(Enum):
    FLOAT = 0
    INT = 1


class ResourceTypeBase:
    def __init__(self, name: T_TranslationOrStr, description: T_TranslationOrStr, _type: ResourceType):
        self._type_name: T_TranslationOrStr = name
        self._type_description: T_TranslationOrStr = description
        self._type_num: ResourceType = _type


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


class Resource:
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
        self._key: str = key
        self._name: T_TranslationOrStr = name
        self._value: ResourceValueType = value
        self._value_storage: ResourceValueType = configure_as_float_or_int
        self._icon: T_TranslationOrStr = icon
        self._description: T_TranslationOrStr = description
        self._type = _type

    @property
    def key(self):
        return self._key

    @key.setter
    def key(self, value):
        self._key = value

    @property
    def name(self) -> T_TranslationOrStr:
        return self._name

    @name.setter
    def name(self, value: T_TranslationOrStr) -> None:
        self._name = value

    @property
    def value(self) -> ResourceValueType:
        return self._value

    @value.setter
    def value(self, value: ResourceValueType) -> None:
        self._value = value

    @property
    def icon(self) -> T_TranslationOrStr:
        return self._icon

    @icon.setter
    def icon(self, value: T_TranslationOrStr) -> None:
        self._icon = value

    @property
    def description(self) -> T_TranslationOrStr:
        return self._description

    @description.setter
    def description(self, value: T_TranslationOrStr) -> None:
        self._description = value

    def __add__(self, other: Union["Resource", float, int]) -> Union[float, int]:
        if isinstance(other, Resource):
            return self._value + other._value
        return self._value + other

    def __sub__(self, other: Union["Resource", float, int]) -> Union[float, int]:
        if isinstance(other, Resource):
            return self._value - other._value
        return self._value - other

    def __mul__(self, other: Union["Resource", float, int]) -> Union[float, int]:
        if isinstance(other, Resource):
            return self._value * other._value
        return self._value * other

    def __truediv__(self, other: Union["Resource", float, int]) -> float:
        if isinstance(other, Resource):
            return self._value / other._value
        return self._value / other

    def __floordiv__(self, other: Union["Resource", float, int]) -> int:
        if isinstance(other, Resource):
            return self._value // other._value
        return self._value // other

    def __mod__(self, other: Union["Resource", float, int]) -> Union[float, int]:
        if isinstance(other, Resource):
            return self._value % other._value
        return self._value % other

    def __pow__(self, other: Union["Resource", float, int]) -> Union[float, int]:
        if isinstance(other, Resource):
            return self._value**other._value
        return self._value**other

    @classmethod
    def strategic(cls, *args, **kwargs) -> "Resource":
        return cls(*args, **kwargs, _type=ResourceTypeStrategic)

    @classmethod
    def luxury(cls, *args, **kwargs) -> "Resource":
        return cls(*args, **kwargs, _type=ResourceTypeLuxury)

    @classmethod
    def bonus(cls, *args, **kwargs) -> "Resource":
        return cls(*args, **kwargs, _type=ResourceTypeBonus)
