import pytest
from openciv.engine.additions.pyload import PyLoad
from openciv.gameplay.techs.trees.core import Core
from openciv.gameplay.tech import Tech
from openciv.engine.managers.log import LogManager

LogManager.get_instance().set_testing_mode(True)


def Techs():
    return list(PyLoad.load_classes("openciv/gameplay/techs/", base_classes=[Tech]).values())


def test_no_duplicate_requires():
    core = Core()
    tech_with_duplicates = []

    for tech in core._items:
        tech_set = set()
        duplicates = set()
        if hasattr(tech, "requires"):
            for requirement in tech.requires:
                if requirement in tech_set:
                    duplicates.add(requirement)
                else:
                    tech_set.add(requirement)
            if duplicates:
                tech_with_duplicates.append((tech, duplicates))
    assert not tech_with_duplicates, f"Found duplicates in tech requires: {tech_with_duplicates}"


def test_all_techs_loaded():
    core = Core()
    all_techs_names = list(PyLoad.load_classes("openciv/gameplay/techs/").keys())
    loaded_tech = [tech.__class__.__name__ for tech in core._items]

    # Find missing techs
    missing_techs = [tech for tech in all_techs_names if tech not in loaded_tech]
    # Find extra techs
    extra_techs = [tech for tech in loaded_tech if tech not in all_techs_names]

    # Remove core as core is the tech tree its self.
    if "Core" in missing_techs:
        missing_techs.remove("Core")

    assert not missing_techs, f"Missing techs: {missing_techs}"
    assert not extra_techs, f"Extra techs: {extra_techs}"


@pytest.mark.parametrize("tech", Techs())
def test_tech_objects(tech: Tech):
    _instance = tech()
    assert isinstance(_instance, Tech)
    assert _instance.key is not None
    assert _instance.name is not None
    assert _instance.description is not None
    assert _instance.tech_points_required is not None
