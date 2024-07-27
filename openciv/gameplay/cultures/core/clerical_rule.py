from openciv.gameplay.culture import Civic
from openciv.engine.managers.i18n import _t


class ClericalRule(Civic):
    def __init__(self, *args, **kwargs):
        super().__init__(
            key="core.culture.civics.clerical_rule",
            name=_t("content.culture.civics.core.clerical_rule.name"),
            description=_t("content.culture.civics.core.clerical_rule.description"),
            *args,
            **kwargs,
        )