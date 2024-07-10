import pytest
from openciv.engine.additions.pyload import PyLoad
from openciv.gameplay.improvement import Improvement


@pytest.mark.nondestructive
def test_load_all_improvements():
    classes = PyLoad.load_classes("openciv/gameplay/improvements/core/")
    for _, _class in classes.items():
        instance = _class()
        assert isinstance(instance, Improvement) or issubclass(instance, Improvement)
