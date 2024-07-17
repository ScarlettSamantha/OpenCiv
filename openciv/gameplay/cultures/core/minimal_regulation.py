from openciv.gameplay.culture import Civic
from openciv.engine.managers.i18n import _t


class MinimalRegulation(Civic):
    def __init__(self, *args, **kwargs):
        super().__init__(
            key="core.culture.civics.minimal_regulation",
            name=_t("content.culture.civics.core.minimal_regulation.name"),
            description=_t("content.culture.civics.core.minimal_regulation.description"),
            *args,
            **kwargs,
        )
