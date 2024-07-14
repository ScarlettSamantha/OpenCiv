from openciv.gameplay.cultures.core.subs._base import BaseCoreSubtree
from openciv.engine.managers.i18n import _t


class Socialism(BaseCoreSubtree):
    def __init__(self, *args, **kwargs):
        super().__init__(
            key="core.culture.subtrees.socialism",
            name=_t("content.culture.subtrees.core.socialism.name"),
            description=_t("content.culture.subtrees.core.socialism.description"),
            *args,
            **kwargs,
        )
