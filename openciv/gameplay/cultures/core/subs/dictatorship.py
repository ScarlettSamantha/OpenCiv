from openciv.gameplay.cultures.core.subs._base import BaseCoreSubtree
from openciv.engine.managers.i18n import _t


class Dictatorship(BaseCoreSubtree):
    def __init__(self):
        super().__init__(
            key="core.culture.subtrees.dictatorship",
            name=_t("content.culture.subtrees.core.dictatorship.name"),
            description=_t("content.culture.subtrees.core.dictatorship.description"),
        )
