from openciv.gameplay.cultures.core.subs._base import BaseCoreSubtree
from openciv.engine.managers.i18n import _t


class Salvery(BaseCoreSubtree):
    def __init__(self):
        super().__init__(
            key="core.culture.subtrees.slavery",
            name=_t("content.culture.subtrees.core.slavery.name"),
            description=_t("content.culture.subtrees.core.slavery.description"),
        )
