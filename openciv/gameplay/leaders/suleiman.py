from __future__ import annotations

from openciv.gameplay.leader import Leader
from openciv.gameplay.effect import Effects
from openciv.engine.managers.i18n import t_


class Suleiman(Leader):
    def __init__(self) -> None:
        super().__init__(
            key="core.leaders.suleiman",
            name=t_("civilization.ottoman.leaders.suleiman.name"),
            description=t_("civilization.ottoman.leaders.suleiman.description"),
            icon="civilization/ottoman/leaders/suleiman/leader_icon.png",
        )
        self._effects = Effects()
