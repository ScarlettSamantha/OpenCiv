from openciv.gameplay.culture import Civic
from openciv.engine.managers.i18n import _t


class DirectAction(Civic):
    def __init__(self, *args, **kwargs):
        super().__init__(
            key="core.culture.civics.direct_action",
            name=_t("content.culture.civics.core.direct_action.name"),
            description=_t("content.culture.civics.core.direct_action.description"),
            *args,
            **kwargs,
        )
