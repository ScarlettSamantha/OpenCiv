from openciv.gameplay.culture import Civic
from openciv.engine.managers.i18n import _t


class VoluntaryAssociations(Civic):
    def __init__(self, *args, **kwargs):
        super().__init__(
            key="core.culture.civics.voluntary_associations",
            name=_t("content.culture.civics.core.voluntary_associations.name"),
            description=_t("content.culture.civics.core.voluntary_associations.description"),
            *args,
            **kwargs,
        )
