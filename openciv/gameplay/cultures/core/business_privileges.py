from __future__ import annotations
from openciv.gameplay.culture import Civic
from openciv.engine.managers.i18n import _t


class BusinessPrivileges(Civic):
    def __init__(self, *args, **kwargs):
        super().__init__(
            key="core.culture.civics.business_privileges",
            name=_t("content.culture.civics.core.business_privileges.name"),
            description=_t("content.culture.civics.core.business_privileges.description"),
            *args,
            **kwargs,
        )
