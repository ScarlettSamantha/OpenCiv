from openciv.gameplay.cultures.core.subs._base import BaseCoreSubtree
from openciv.engine.managers.i18n import _t


class Nationalism(BaseCoreSubtree):
    def __init__(self, *args, **kwargs):
        super().__init__(
            key="core.culture.subtrees.nationalism",
            name=_t("content.culture.subtrees.core.nationalism.name"),
            description=_t("content.culture.subtrees.core.nationalism.description"),
            *args,
            **kwargs,
        )
