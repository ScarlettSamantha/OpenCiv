from __future__ import annotations
from openciv.gameplay.culture import Civic
from openciv.engine.managers.i18n import _t


class MoralLegislation(Civic):
    def __init__(self, *args, **kwargs):
        super().__init__(
            key="core.culture.civics.moral_legislation",
            name=_t("content.culture.civics.core.moral_legislation.name"),
            description=_t("content.culture.civics.core.moral_legislation.description"),
            *args,
            **kwargs,
        )
