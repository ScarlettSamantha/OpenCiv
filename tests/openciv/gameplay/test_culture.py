from __future__ import annotations
from openciv.gameplay.cultures.core.tree.core import CoreCultureTree
from openciv.engine.additions.pyload import PyLoad
from openciv.gameplay.culture import Civic
import pytest


def cultures():
    cultures = PyLoad.load_classes("openciv/gameplay/cultures/", base_classes=Civic)
    return list(cultures.values())


def test_core_culture_tree():
    instance = CoreCultureTree()

    assert instance.key == "core.culture.tree"
    assert instance._load_subclasses().values().__len__() == instance.subtrees.__len__()


def test_load_subtress():
    instances = PyLoad.load_classes("openciv/gameplay/cultures/core/subs", lambda x: not x.startswith("_"))
    for _, instance in instances.items():
        _instance = instance()
        _instance.register_civics()
    assert True


@pytest.mark.parametrize("class_ref", cultures())
def test_culture_initialization(class_ref: Civic):
    culture_instance: Civic = class_ref()

    assert isinstance(culture_instance, Civic), f"{class_ref.__name__} is not an instance of Civic"
    assert culture_instance.key is not None, f"{class_ref.__class__.__name__} has no key"
    assert culture_instance.name is not None, f"{class_ref.__class__.__name__} has no name"
    assert culture_instance.description is not None, f"{class_ref.__class__.__name__} has no description"
