from openciv.gameplay.cultures.core.subs._base import BaseCoreSubtree
from openciv.engine.managers.i18n import _t


class Corporatocracy(BaseCoreSubtree):
    def __init__(
        self,
    ):
        super().__init__(
            key="core.culture.subtrees.corporatocracy",
            name=_t("content.culture.subtrees.core.corporatocracy.name"),
            description=_t("content.culture.subtrees.core.corporatocracy.description"),
        )
