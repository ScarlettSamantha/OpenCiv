from openciv.gameplay.cultures.core.subs._base import BaseCoreSubtree
from openciv.engine.managers.i18n import _t


class Oligarchy(BaseCoreSubtree):
    def __init__(self):
        super().__init__(
            key="core.culture.subtrees.oligarchy",
            name=_t("content.culture.subtrees.core.oligarchy.name"),
            description=_t("content.culture.subtrees.core.oligarchy.description"),
        )
