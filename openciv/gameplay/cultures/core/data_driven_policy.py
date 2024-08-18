from __future__ import annotations
from openciv.gameplay.culture import Civic
from openciv.engine.managers.i18n import _t


class DataDrivenPolicy(Civic):
    def __init__(self, *args, **kwargs):
        super().__init__(
            key="core.culture.civics.data_driven_policy",
            name=_t("content.culture.civics.core.data_driven_policy.name"),
            description=_t("content.culture.civics.core.data_driven_policy.description"),
            *args,
            **kwargs,
        )
