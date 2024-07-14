from openciv.gameplay.cultures.core.subs._base import BaseCoreSubtree
from openciv.engine.managers.i18n import _t


class Puritanism(BaseCoreSubtree):
    def __init__(self):
        super().__init__(
            key="core.culture.subtrees.puritanism",
            name=_t("content.culture.subtrees.core.puritanism.name"),
            description=_t("content.culture.subtrees.core.puritanism.description"),
        )
