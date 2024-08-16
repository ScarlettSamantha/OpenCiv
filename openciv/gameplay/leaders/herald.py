from __future__ import annotations

from openciv.gameplay.leader import Leader
from openciv.gameplay.effect import Effects
from openciv.engine.managers.i18n import t_


class Herald(Leader):
    def __init__(self) -> None:
        super().__init__(
            key="core.leaders.herald",
            name=t_("civilization.vikings.leaders.herald.name"),
            description=t_("civilization.vikings.leaders.herald.description"),
            icon="civilization/vikings/leaders/herald/leader_icon.png",
        )
        self._effects = Effects()
