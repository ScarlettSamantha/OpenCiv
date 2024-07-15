from openciv.gameplay.culture import Civic
from openciv.engine.managers.i18n import _t


class ReasonAndLogic(Civic):
    def __init__(self, *args, **kwargs):
        super().__init__(
            key="core.culture.civics.reason_and_logic",
            name=_t("content.culture.civics.core.reason_and_logic.name"),
            description=_t("content.culture.civics.core.reason_and_logic.description"),
            *args,
            **kwargs,
        )
