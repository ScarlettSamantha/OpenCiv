from __future__ import annotations
from openciv.gameplay.culture import Civic
from openciv.engine.managers.i18n import _t


class ProletarianDictatorship(Civic):
    def __init__(self, *args, **kwargs):
        super().__init__(
            key="core.culture.civics.proletarian_dictatorship",
            name=_t("content.culture.civics.core.proletarian_dictatorship.name"),
            description=_t("content.culture.civics.core.proletarian_dictatorship.description"),
            *args,
            **kwargs,
        )
