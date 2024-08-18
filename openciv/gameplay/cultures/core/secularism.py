from __future__ import annotations
from openciv.gameplay.culture import Civic
from openciv.engine.managers.i18n import _t


class Secularism(Civic):
    def __init__(self, *args, **kwargs):
        super().__init__(
            key="core.culture.civics.secularism",
            name=_t("content.culture.civics.core.secularism.name"),
            description=_t("content.culture.civics.core.secularism.description"),
            *args,
            **kwargs,
        )
