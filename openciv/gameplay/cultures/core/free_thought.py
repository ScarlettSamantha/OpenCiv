from openciv.gameplay.culture import Civic
from openciv.engine.managers.i18n import _t


class FreeThought(Civic):
    def __init__(self, *args, **kwargs):
        super().__init__(
            key="core.culture.civics.free_thought",
            name=_t("content.culture.civics.core.free_thought.name"),
            description=_t("content.culture.civics.core.free_thought.description"),
            *args,
            **kwargs,
        )
