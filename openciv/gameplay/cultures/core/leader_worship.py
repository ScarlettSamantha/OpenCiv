from __future__ import annotations
from openciv.gameplay.culture import Civic
from openciv.engine.managers.i18n import _t


class LeaderWorship(Civic):
    def __init__(self, *args, **kwargs):
        super().__init__(
            key="core.culture.civics.leader_worship",
            name=_t("content.culture.civics.core.leader_worship.name"),
            description=_t("content.culture.civics.core.leader_worship.description"),
            *args,
            **kwargs,
        )
