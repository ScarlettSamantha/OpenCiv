from openciv.gameplay.cultures.core.tree.core import CoreCultureTree
from openciv.engine.additions.pyload import PyLoad


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
