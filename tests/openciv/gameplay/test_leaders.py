from openciv.engine.additions.pyload import PyLoad
from openciv.gameplay.effects import Effects
from openciv.gameplay.effect import Effect
from openciv.gameplay.leader import Leader
import pytest

leaders = PyLoad.load_classes("openciv/gameplay/leaders/")


@pytest.mark.parametrize("class_name, class_ref", leaders.items())
def test_leader_initialization(class_name, class_ref):
    """
    Test the initialization of different Leader implementations.
    """
    leader_instance = class_ref()

    assert isinstance(leader_instance, Leader), f"{class_name} is not an instance of Leader"
    assert leader_instance.name is not None, f"{class_name} has no name"
    assert leader_instance.icon is not None, f"{class_name} has no icon"
    assert leader_instance.description is not None, f"{class_name} has no description"
    assert isinstance(leader_instance._effects, Effects), f"{class_name} has incorrect _effects type"
    assert leader_instance._effects.effects == {}, f"{class_name} has non-empty _effects"


@pytest.mark.parametrize("class_name, class_ref", leaders.items())
def test_leader_effects(class_name, class_ref):
    """
    Test the effects functionality of different Leader implementations.
    """
    leader_instance: Leader = class_ref()
    effect = Effect("Test", target="Test", domain=None)
    leader_instance.add_effect(effect)

    assert effect in leader_instance._effects.effects.values(), f"{class_name} failed to add effect"
