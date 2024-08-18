from __future__ import annotations
from openciv.gameplay.culture import Civic
from openciv.engine.managers.i18n import _t


class EliteRule(Civic):
    def __init__(self, *args, **kwargs):
        super().__init__(
            key="core.culture.civics.elite_rule",
            name=_t("content.culture.civics.core.elite_rule.name"),
            description=_t("content.culture.civics.core.elite_rule.description"),
            *args,
            **kwargs,
        )
