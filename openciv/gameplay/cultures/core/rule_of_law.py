from __future__ import annotations
from openciv.gameplay.culture import Civic
from openciv.engine.managers.i18n import _t


class RuleOfLaw(Civic):
    def __init__(self, *args, **kwargs):
        super().__init__(
            key="core.culture.civics.rule_of_law",
            name=_t("content.culture.civics.core.rule_of_law.name"),
            description=_t("content.culture.civics.core.rule_of_law.description"),
            *args,
            **kwargs,
        )
