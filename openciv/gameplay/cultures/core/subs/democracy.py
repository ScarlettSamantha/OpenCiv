from openciv.gameplay.cultures.core.subs._base import BaseCoreSubtree
from openciv.engine.managers.i18n import _t


class Democracy(BaseCoreSubtree):
    def __init__(self):
        super().__init__(
            key="core.culture.subtrees.democracy",
            name=_t("content.culture.subtrees.core.democracy.name"),
            description=_t("content.culture.subtrees.core.democracy.description"),
        )
