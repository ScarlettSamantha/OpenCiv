from openciv.gameplay.culture import Civic
from openciv.engine.managers.i18n import _t


class CapitalAccumulation(Civic):
    def __init__(self, *args, **kwargs):
        super().__init__(
            key="core.culture.civics.capital_accumulation",
            name=_t("content.culture.civics.core.capital_accumulation.name"),
            description=_t("content.culture.civics.core.capital_accumulation.description"),
            *args,
            **kwargs,
        )
