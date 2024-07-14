from openciv.gameplay.cultures.core.subs._base import BaseCoreSubtree
from openciv.engine.managers.i18n import _t


class Fascism(BaseCoreSubtree):
    def __init__(self, *args, **kwargs):
        super().__init__(
            key="core.culture.subtrees.facism",
            name=_t("content.culture.subtrees.core.facism.name"),
            description=_t("content.culture.subtrees.core.facism.description"),
            *args,
            **kwargs,
        )
