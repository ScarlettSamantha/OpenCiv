from openciv.gameplay.cultures.core.subs._base import BaseCoreSubtree
from openciv.engine.managers.i18n import _t


class Technocracy(BaseCoreSubtree):
    def __init__(self, *args, **kwargs):
        super().__init__(
            key="core.culture.subtrees.technocracy",
            name=_t("content.culture.subtrees.core.technocracy.name"),
            description=_t("content.culture.subtrees.core.technocracy.description"),
            *args,
            **kwargs,
        )
