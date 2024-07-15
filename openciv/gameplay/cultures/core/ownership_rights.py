from openciv.gameplay.culture import Civic
from openciv.engine.managers.i18n import _t


class OwnershipRights(Civic):
    def __init__(self, *args, **kwargs):
        super().__init__(
            key="core.culture.civics.ownership_rights",
            name=_t("content.culture.civics.core.ownership_rights.name"),
            description=_t("content.culture.civics.core.ownership_rights.description"),
            *args,
            **kwargs,
        )
