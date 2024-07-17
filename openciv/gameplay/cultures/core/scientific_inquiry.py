from openciv.gameplay.culture import Civic
from openciv.engine.managers.i18n import _t


class ScientificInquiry(Civic):
    def __init__(self, *args, **kwargs):
        super().__init__(
            key="core.culture.civics.scientific_inquiry",
            name=_t("content.culture.civics.core.scientific_inquiry.name"),
            description=_t("content.culture.civics.core.scientific_inquiry.description"),
            *args,
            **kwargs,
        )
