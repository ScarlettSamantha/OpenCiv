from openciv.gameplay.cultures.core.subs._base import BaseCoreSubtree
from openciv.engine.managers.i18n import _t


class Communism(BaseCoreSubtree):
    def __init__(self, *args, **kwargs):
        super().__init__(
            key="core.culture.subtrees.communism",
            name=_t("content.culture.subtrees.core.communism.name"),
            description=_t("content.culture.subtrees.core.communism.description"),
            *args,
            **kwargs,
        )
