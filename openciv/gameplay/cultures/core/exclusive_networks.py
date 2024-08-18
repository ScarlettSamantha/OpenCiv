from __future__ import annotations
from openciv.gameplay.culture import Civic
from openciv.engine.managers.i18n import _t


class ExclusiveNetworks(Civic):
    def __init__(self, *args, **kwargs):
        super().__init__(
            key="core.culture.civics.exclusive_networks",
            name=_t("content.culture.civics.core.exclusive_networks.name"),
            description=_t("content.culture.civics.core.exclusive_networks.description"),
            *args,
            **kwargs,
        )
