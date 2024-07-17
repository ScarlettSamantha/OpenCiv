from openciv.gameplay.culture import Civic
from openciv.engine.managers.i18n import _t


class CorporateInfluence(Civic):
    def __init__(self, *args, **kwargs):
        super().__init__(
            key="core.culture.civics.corporate_influence",
            name=_t("content.culture.civics.core.corporate_influence.name"),
            description=_t("content.culture.civics.core.corporate_influence.description"),
            *args,
            **kwargs,
        )
