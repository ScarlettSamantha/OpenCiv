from openciv.gameplay.cultures.core.subs._base import BaseCoreSubtree
from openciv.engine.managers.i18n import _t


class Liberalism(BaseCoreSubtree):
    def __init__(self, *args, **kwargs):
        super().__init__(
            key="core.culture.subtrees.liberalism",
            name=_t("content.culture.subtrees.core.liberalism.name"),
            description=_t("content.culture.subtrees.core.liberalism.description"),
            *args,
            **kwargs,
        )
