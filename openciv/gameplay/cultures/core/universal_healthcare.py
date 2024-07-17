from openciv.gameplay.culture import Civic
from openciv.engine.managers.i18n import _t


class UniversalHealthcare(Civic):
    def __init__(self, *args, **kwargs):
        super().__init__(
            key="core.culture.civics.universal_healthcare",
            name=_t("content.culture.civics.core.universal_healthcare.name"),
            description=_t("content.culture.civics.core.universal_healthcare.description"),
            *args,
            **kwargs,
        )
