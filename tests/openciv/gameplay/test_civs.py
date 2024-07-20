import pytest
from openciv.gameplay.civilization import Civilization
from openciv.engine.additions.pyload import PyLoad


def civs():
    civs = PyLoad.load_classes("openciv/gameplay/civilizations/")
    return list(civs.values())


@pytest.mark.parametrize("class_ref", civs())
def test_civ_initialization(class_ref: Civilization):
    """
    Test the initialization of different Civ implementations.
    """
    civ_instance: Civilization = class_ref()

    assert isinstance(civ_instance, Civilization), f"{class_ref.__class__.__name__} is not an instance of Civ"
    assert civ_instance.name is not None, f"{class_ref.__class__.__name__} has no name"
    assert civ_instance.icon is not None, f"{class_ref.__class__.__name__} has no icon"
    assert civ_instance.description is not None, f"{class_ref.__class__.__name__} has no description"
