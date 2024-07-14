from openciv.gameplay.cultures.core.subs._base import BaseCoreSubtree
from openciv.engine.managers.i18n import _t


class Monarchy(BaseCoreSubtree):
    def __init__(self):
        super().__init__(
            key="core.culture.subtrees.monarchy",
            name=_t("content.culture.subtrees.core.monarchy.name"),
            description=_t("content.culture.subtrees.core.monarchy.description"),
        )
