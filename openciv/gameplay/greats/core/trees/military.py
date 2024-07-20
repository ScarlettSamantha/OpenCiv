from openciv.gameplay.greats.core.trees._base import BaseCoreGreatsTree
from openciv.engine.managers.i18n import _t


class MilitaryGreatsTree(BaseCoreGreatsTree):
    def __init__(self):
        super().__init__(
            key="core.greats.tree.military",
            name=_t("content.greats.core.trees.military.name"),
            description=_t("content.greats.core.trees.military.description"),
        )
        self.load_folder = "core/military/"

        # Do this before saving so we can save the greats we loaded.
        self.load_greats_from_folder()

        self._setup_saveable()
