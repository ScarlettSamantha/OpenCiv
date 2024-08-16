from __future__ import annotations

from openciv.gameplay.leader import Leader
from openciv.gameplay.effect import Effects
from openciv.engine.managers.i18n import t_


class Phillip(Leader):
    def __init__(self) -> None:
        super().__init__(
            key="core.leaders.phillip",
            name=t_("civilization.spain.leaders.phillip.name"),
            description=t_("civilization.spain.leaders.phillip.description"),
            icon="civilization/spain/leaders/phillip/leader_icon.png",
        )
        self._effects = Effects()
