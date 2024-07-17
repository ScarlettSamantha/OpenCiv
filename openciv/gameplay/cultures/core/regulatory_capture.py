from openciv.gameplay.culture import Civic
from openciv.engine.managers.i18n import _t


class RegulatoryCapture(Civic):
    def __init__(self, *args, **kwargs):
        super().__init__(
            key="core.culture.civics.regulatory_capture",
            name=_t("content.culture.civics.core.regulatory_capture.name"),
            description=_t("content.culture.civics.core.regulatory_capture.description"),
            *args,
            **kwargs,
        )
