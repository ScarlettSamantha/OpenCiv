from openciv.gameplay.cultures.core.subs._base import BaseCoreSubtree
from openciv.engine.managers.i18n import _t


class Capitalism(BaseCoreSubtree):
    def __init__(self, *args, **kwargs):
        super().__init__(
            key="core.culture.subtrees.capitalism",
            name=_t("content.culture.subtrees.core.capitalism.name"),
            description=_t("content.culture.subtrees.core.capitalism.description"),
            *args,
            **kwargs,
        )
