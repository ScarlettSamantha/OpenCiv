from __future__ import annotations
from openciv.engine.additions.pyload import PyLoad
from openciv.engine.managers.i18n import t_
from openciv.gameplay.effect import Effect, Effects
from openciv.gameplay.leader import Leader
import pytest
from typing import Type, Dict


def leaders() -> Dict[str, Type[Leader]]:
    leaders: Dict[str, Type[Leader]] = PyLoad.load_classes(directory="openciv/gameplay/leaders/")
    return leaders


@pytest.mark.parametrize("class_name, class_ref", leaders().items())
def test_leader_initialization(class_name: str, class_ref: Type[Leader]) -> None:
    """
    Test the initialization of different Leader implementations.
    """
    leader_instance = class_ref()  # type: ignore

    assert isinstance(leader_instance, Leader), f"{class_name} is not an instance of Leader"
    assert leader_instance.name is not None, f"{class_name} has no name"
    assert leader_instance.icon is not None, f"{class_name} has no icon"
    assert leader_instance.description is not None, f"{class_name} has no description"
    assert isinstance(leader_instance.effects, Effects), f"{class_name} has incorrect _effects type"
    assert leader_instance.effects.effects == {}, f"{class_name} has non-empty _effects"


@pytest.mark.parametrize("class_name, class_ref", leaders().items())
def test_leader_effects(class_name: str, class_ref: Type[Leader]) -> None:
    """
    Test the effects functionality of different Leader implementations.
    """
    leader_instance: Leader = class_ref()  # type: ignore
    effect = Effect(key="Test", target=None, target_type=None, name=t_("Test"), description=t_("Test"), icon="Test")
    leader_instance.add_effect(effect=effect)

    assert effect in leader_instance.effects.effects.values(), f"{class_name} failed to add effect"
