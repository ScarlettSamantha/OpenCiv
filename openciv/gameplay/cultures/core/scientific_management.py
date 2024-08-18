from __future__ import annotations
from openciv.gameplay.culture import Civic
from openciv.engine.managers.i18n import _t


class ScientificManagement(Civic):
    def __init__(self, *args, **kwargs):
        super().__init__(
            key="core.culture.civics.scientific_management",
            name=_t("content.culture.civics.core.scientific_management.name"),
            description=_t("content.culture.civics.core.scientific_management.description"),
            *args,
            **kwargs,
        )
