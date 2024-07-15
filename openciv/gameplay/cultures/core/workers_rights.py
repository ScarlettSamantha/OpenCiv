from openciv.gameplay.culture import Civic
from openciv.engine.managers.i18n import _t


class WorkersRights(Civic):
    def __init__(self, *args, **kwargs):
        super().__init__(
            key="core.culture.civics.workers_rights",
            name=_t("content.culture.civics.core.workers_rights.name"),
            description=_t("content.culture.civics.core.workers_rights.description"),
            *args,
            **kwargs,
        )
