from openciv.gameplay.cultures.core.subs._base import BaseCoreSubtree
from openciv.engine.managers.i18n import _t


class Theocracy(BaseCoreSubtree):
    def __init__(self, *args, **kwargs):
        super().__init__(
            key="core.culture.subtrees.theocracy",
            name=_t("content.culture.subtrees.core.theocracy.name"),
            description=_t("content.culture.subtrees.core.theocracy.description"),
            *args,
            **kwargs,
        )
