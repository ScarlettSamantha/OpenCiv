from __future__ import annotations

from openciv.gameplay.leader import Leader
from openciv.gameplay.effect import Effects
from openciv.engine.managers.i18n import t_


class SittingBull(Leader):
    def __init__(self) -> None:
        super().__init__(
            key="core.leaders.sitting_bull",
            name=t_("civilization.american_empire.leaders.sitting_bull.name"),
            description=t_("civilization.american_empire.leaders.sitting_bull.description"),
            icon="civilization/american_empire/leaders/sitting_bull/leader_icon.png",
        )
        self._effects = Effects()
