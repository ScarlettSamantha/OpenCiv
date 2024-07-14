from openciv.gameplay.cultures.core.subs._base import BaseCoreSubtree
from openciv.engine.managers.i18n import _t


class Unionism(BaseCoreSubtree):
    def __init__(self):
        super().__init__(
            key="core.culture.subtrees.unionism",
            name=_t("content.culture.subtrees.core.unionism.name"),
            description=_t("content.culture.subtrees.core.unionism.description"),
        )
