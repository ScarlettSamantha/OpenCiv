from openciv.gameplay.greats.core.trees._base import BaseCoreGreatsTree
from openciv.engine.managers.i18n import _t


class ExplorersGreatsTree(BaseCoreGreatsTree):
    def __init__(self):
        super().__init__(
            key="core.greats.tree.explorers",
            name=_t("content.greats.core.trees.explorers.name"),
            description=_t("content.greats.core.trees.explorers.description"),
        )
        self.load_folder = "core/explorers/"

        # Do this before saving so we can save the greats we loaded.
        self.load_greats_from_folder()

        self._setup_saveable()
