from __future__ import annotations
from openciv.gameplay.culture import Civic
from openciv.engine.managers.i18n import _t


class StatePropaganda(Civic):
    def __init__(self, *args, **kwargs):
        super().__init__(
            key="core.culture.civics.state_propaganda",
            name=_t("content.culture.civics.core.state_propaganda.name"),
            description=_t("content.culture.civics.core.state_propaganda.description"),
            *args,
            **kwargs,
        )
