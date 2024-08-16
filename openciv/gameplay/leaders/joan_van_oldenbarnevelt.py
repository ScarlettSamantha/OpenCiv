from __future__ import annotations

from openciv.gameplay.leader import Leader
from openciv.gameplay.effect import Effects
from openciv.engine.managers.i18n import t_


class JoanVanOldenbarnevelt(Leader):
    def __init__(self) -> None:
        super().__init__(
            key="core.leaders.joan_van_oldenbarnevelt",
            name=t_("civilization.low_countries.leaders.joan_van_oldenbarnevelt.name"),
            description=t_("civilization.low_countries.leaders.joan_van_oldenbarnevelt.description"),
            icon="civilization/low_countries/leaders/joan_van_oldenbarnevelt/leader_icon.png",
        )
        self._effects = Effects()
