from openciv.gameplay.cultures.core.subs._base import BaseCoreSubtree
from openciv.engine.managers.i18n import _t


class Anarchy(BaseCoreSubtree):
    def __init__(self, *args, **kwargs):
        super().__init__(
            key="core.culture.subtrees.anarchy",
            name=_t("content.culture.subtrees.core.anarchy.name"),
            description=_t("content.culture.subtrees.core.anarchy.description"),
            *args,
            **kwargs,
        )
