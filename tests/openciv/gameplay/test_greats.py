from __future__ import annotations
import pytest
from openciv.engine.additions.pyload import PyLoad
from openciv.gameplay.greats.core.trees._base import GreatsTree
from openciv.gameplay.greats.core._base import Great
from typing import Dict, Callable


def load_greats() -> Dict[str, Callable]:
    return PyLoad.load_classes("openciv/gameplay/greats/core", base_classes=[Great])


def test_greats_trees_proper_type():
    trees: Dict[str, Callable] = PyLoad.load_classes("openciv/gameplay/greats/core/trees/")
    assert all([callable(tree) for tree in trees.values()])
    assert all([issubclass(tree, GreatsTree) for tree in trees.values()])


def test_greats_tree_instancable():
    trees: Dict[str, Callable] = PyLoad.load_classes("openciv/gameplay/greats/core/trees/")
    for _, tree in trees.items():
        _instance = tree()
        assert isinstance(_instance, GreatsTree)


def test_greats_tree_registration():
    trees: Dict[str, Callable] = PyLoad.load_classes("openciv/gameplay/greats/core/trees/")
    engineering_tree = None
    for _, tree in trees.items():
        _instance = tree()
        if _instance.key == "core.greats.tree.engineers":
            engineering_tree = _instance
        assert isinstance(_instance, GreatsTree)
    assert engineering_tree is not None, "Engineering Tree not found"
    assert any(
        [great().key == "core.engineers.guido" for great in engineering_tree.greats]
    ), "Guido not found in Engineering Tree"


@pytest.mark.parametrize("great", load_greats().values())
def test_instance_greats(great: Callable[[], Great]):
    _instance = great()
    assert isinstance(_instance, Great)
    assert _instance.key is not None
    assert _instance.name is not None
    assert _instance.description is not None
    assert _instance.cost is not None
