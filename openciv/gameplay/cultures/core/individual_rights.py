from openciv.gameplay.culture import Civic
from openciv.engine.managers.i18n import _t


class IndividualRights(Civic):
    def __init__(self, *args, **kwargs):
        super().__init__(
            key="core.culture.civics.individual_rights",
            name=_t("content.culture.civics.core.individual_rights.name"),
            description=_t("content.culture.civics.core.individual_rights.description"),
            *args,
            **kwargs,
        )
