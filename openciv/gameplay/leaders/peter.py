from __future__ import annotations

from openciv.gameplay.leader import Leader
from openciv.gameplay.effect import Effects
from openciv.engine.managers.i18n import t_


class Peter(Leader):
    def __init__(self) -> None:
        super().__init__(
            key="core.leaders.peter",
            name=t_("civilization.ussr.leaders.peter.name"),
            description=t_("civilization.ussr.leaders.peter.description"),
            icon="civilization/ussr/leaders/peter/leader_icon.png",
        )
        self._effects = Effects()
