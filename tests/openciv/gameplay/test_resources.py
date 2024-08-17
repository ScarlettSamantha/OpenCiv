from __future__ import annotations

from typing import Any, Dict
import pytest
from openciv.gameplay.resource import (
    Resource,
    ResourceTypeBase,
    Resources,
    ResourceTypeBonus,
    ResourceTypeLuxury,
    ResourceTypeStrategic,
)
from openciv.engine.exceptions.resource_exception import ResourceTypeException
from openciv.engine.managers.i18n import t_


def test_resource_initialization() -> None:
    name = t_("test.resource.name")
    description = t_("test.resource.description")
    icon = t_("test.resource.icon")
    resource = Resource(
        key="testkey", name=name, type_=ResourceTypeBonus, value=100, icon=icon, description=description
    )

    assert resource.name == name
    assert resource.value == 100
    assert resource.icon == icon
    assert resource.description == description
    assert resource.type == ResourceTypeBonus


def test_resource_property_setters() -> None:
    resource = Resource(key="testkey", name=t_("test.resource.name"), type_=ResourceTypeBonus, value=100)
    new_name = t_("test.resource.new_name")
    new_value = 200
    new_icon = t_("test.resource.new_icon")
    new_description = t_("test.resource.new_description")

    resource.name = new_name
    resource.value = new_value
    resource.icon = new_icon
    resource.description = new_description

    assert resource.name == new_name
    assert resource.value == new_value
    assert resource.icon == new_icon
    assert resource.description == new_description


def test_resource_arithmetic_operations() -> None:
    resource1 = Resource(key="testkey", name=t_("resource1"), type_=ResourceTypeBonus, value=100)
    resource2 = Resource(key="testkey", name=t_("resource2"), type_=ResourceTypeBonus, value=50)

    assert resource1 + resource2 == 150
    assert resource1 - resource2 == 50
    assert resource1 * resource2 == 5000
    assert resource1 / resource2 == 2.0
    assert resource1 // resource2 == 2
    assert resource1 % resource2 == 0
    assert resource1**resource2 == 100**50


def test_resource_class_methods() -> None:
    name = t_("test.resource.name")
    value = 100
    strategic_resource: Resource = Resource.strategic(key="testkey", name=name, value=value)
    luxury_resource: Resource = Resource.luxury(key="testkey", name=name, value=value)
    bonus_resource: Resource = Resource.bonus(key="testkey", name=name, value=value)

    assert strategic_resource.type == ResourceTypeStrategic
    assert luxury_resource.type == ResourceTypeLuxury
    assert bonus_resource.type == ResourceTypeBonus


def test_resources_initialization() -> None:
    resources = Resources()

    assert isinstance(resources.resources[ResourceTypeBonus], dict)
    assert isinstance(resources.resources[ResourceTypeStrategic], dict)
    assert isinstance(resources.resources[ResourceTypeLuxury], dict)


def test_resources_add_and_get() -> None:
    resources = Resources()
    resource = Resource(key="testkey", name=t_("test.resource.name"), type_=ResourceTypeBonus, value=100)

    resources.add(resource=resource)
    retrieved_resource: Resource = resources.get(_type=ResourceTypeBonus, key="testkey")  # type: ignore | this is a test its kind of the point
    assert isinstance(retrieved_resource, Resource)
    assert retrieved_resource.name == resource.name
    assert retrieved_resource.value == resource.value


def test_resources_add_exception() -> None:
    resources = Resources()
    with pytest.raises(expected_exception=ResourceTypeException):
        resources + "Not a Resource"  # type: ignore | this is a test its kind of the point


def test_resources_to_dict():
    resources = Resources()
    resource = Resource(key="testkey", name=t_("test.resource.name"), type_=ResourceTypeBonus, value=100)
    resources.add(resource=resource)
    resources_dict: Dict[type[ResourceTypeBase], Dict[str, Resource]] = resources.toDict()

    assert isinstance(resources_dict, dict)
    assert isinstance(resources_dict[ResourceTypeBonus], dict)
    assert "testkey" in resources_dict[ResourceTypeBonus]
    assert resources_dict[ResourceTypeBonus]["testkey"].name == t_("test.resource.name")


def test_loading_resources():
    from openciv.engine.additions.pyload import PyLoad

    pyload: Dict[str, Any] = PyLoad.load_classes(directory="openciv/gameplay/resources/", base_classes=[Resource])
    for _, resource in pyload.items():
        instance = resource(0.0)
        assert isinstance(instance, Resource)
