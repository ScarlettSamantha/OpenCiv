import pytest
from openciv.gameplay.resource import (
    Resource,
    Resources,
    ResourceTypeBonus,
    ResourceTypeLuxury,
    ResourceTypeStrategic,
)
from openciv.engine.exceptions.resource_exception import ResourceTypeException
from openciv.engine.managers.i18n import _t


def test_resource_initialization():
    name = _t("test.resource.name")
    description = _t("test.resource.description")
    icon = _t("test.resource.icon")
    resource = Resource("testkey", name, ResourceTypeBonus, 100, icon=icon, description=description)

    assert resource.name == name
    assert resource.value == 100
    assert resource._icon == icon
    assert resource.description == description
    assert resource._type == ResourceTypeBonus


def test_resource_property_setters():
    resource = Resource("testkey", _t("test.resource.name"), ResourceTypeBonus, 100)
    new_name = _t("test.resource.new_name")
    new_value = 200
    new_icon = _t("test.resource.new_icon")
    new_description = _t("test.resource.new_description")

    resource.name = new_name
    resource.value = new_value
    resource.icon = new_icon
    resource.description = new_description

    assert resource.name == new_name
    assert resource.value == new_value
    assert resource.icon == new_icon
    assert resource.description == new_description


def test_resource_arithmetic_operations():
    resource1 = Resource("testkey", _t("resource1"), ResourceTypeBonus, 100)
    resource2 = Resource("testkey", _t("resource2"), ResourceTypeBonus, 50)

    assert resource1 + resource2 == 150
    assert resource1 - resource2 == 50
    assert resource1 * resource2 == 5000
    assert resource1 / resource2 == 2.0
    assert resource1 // resource2 == 2
    assert resource1 % resource2 == 0
    assert resource1**resource2 == 100**50


def test_resource_class_methods():
    name = _t("test.resource.name")
    value = 100
    strategic_resource = Resource.strategic(key="testkey", name=name, value=value)
    luxury_resource = Resource.luxury(key="testkey", name=name, value=value)
    bonus_resource = Resource.bonus(key="testkey", name=name, value=value)

    assert strategic_resource._type == ResourceTypeStrategic
    assert luxury_resource._type == ResourceTypeLuxury
    assert bonus_resource._type == ResourceTypeBonus


def test_resources_initialization():
    resources = Resources()

    assert isinstance(resources.resources[ResourceTypeBonus], dict)
    assert isinstance(resources.resources[ResourceTypeStrategic], dict)
    assert isinstance(resources.resources[ResourceTypeLuxury], dict)


def test_resources_add_and_get():
    resources = Resources()
    resource = Resource("testkey", _t("test.resource.name"), ResourceTypeBonus, 100)

    resources.add(resource)
    retrieved_resource = resources.get(ResourceTypeBonus, "testkey")

    assert retrieved_resource.name == resource.name
    assert retrieved_resource.value == resource.value


def test_resources_add_exception():
    resources = Resources()
    with pytest.raises(ResourceTypeException):
        resources + "Not a Resource"


def test_resources_to_dict():
    resources = Resources()
    resource = Resource("testkey", _t("test.resource.name"), ResourceTypeBonus, 100)
    resources.add(resource)
    resources_dict = resources.toDict()

    assert isinstance(resources_dict, dict)
    assert isinstance(resources_dict[ResourceTypeBonus], dict)
    assert "testkey" in resources_dict[ResourceTypeBonus]
    assert resources_dict[ResourceTypeBonus]["testkey"].name == _t("test.resource.name")


def test_loading_resources():
    from openciv.engine.additions.pyload import PyLoad

    pyload = PyLoad.load_classes("openciv/gameplay/resources/")
    for _, resource in pyload.items():
        instance = resource(0.0)
        assert isinstance(instance, Resource)
