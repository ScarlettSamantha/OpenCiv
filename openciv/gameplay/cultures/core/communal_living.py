from __future__ import annotations
from openciv.gameplay.culture import Civic
from openciv.engine.managers.i18n import _t


class CommunalLiving(Civic):
    def __init__(self, *args, **kwargs):
        super().__init__(
            key="core.culture.civics.communal_living",
            name=_t("content.culture.civics.core.communal_living.name"),
            description=_t("content.culture.civics.core.communal_living.description"),
            *args,
            **kwargs,
        )
