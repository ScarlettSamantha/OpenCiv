from __future__ import annotations
from openciv.gameplay.culture import CultureTree
from openciv.engine.managers.i18n import _t

from openciv.engine.additions.pyload import PyLoad


class CoreCultureTree(CultureTree):
    def __init__(self, *args, **kwargs):
        super(*args, **kwargs).__init__(
            key="core.culture.tree",
            name=_t("content.culture.tree.core.name"),
            description=_t("content.culture.tree.core.name"),
        )

    def _load_subclasses(self):
        return PyLoad.load_classes("openciv/gameplay/cultures/core/subs", lambda x: not x.startswith("_"))

    def register_subtrees(self):
        # We just load all the classes in the subs directory and add them as subtrees
        classes = self._load_subclasses()
        for _, subtree in classes.items():
            self.add_subtree(subtree())
