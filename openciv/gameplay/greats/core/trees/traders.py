from __future__ import annotations
from openciv.gameplay.greats.core.trees._base import BaseCoreGreatsTree
from openciv.engine.managers.i18n import _t


class TradersGreatsTree(BaseCoreGreatsTree):
    def __init__(self):
        super().__init__(
            key="core.greats.tree.traders",
            name=_t("content.greats.core.trees.traders.name"),
            description=_t("content.greats.core.trees.traders.description"),
        )
        self.load_folder = "core/traders/"

        # Do this before saving so we can save the greats we loaded.
        self.load_greats_from_folder()

        self._setup_saveable()
