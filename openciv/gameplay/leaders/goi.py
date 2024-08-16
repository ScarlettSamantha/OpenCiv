from __future__ import annotations

from openciv.gameplay.leader import Leader
from openciv.gameplay.effect import Effects
from openciv.engine.managers.i18n import t_


class Goi(Leader):
    def __init__(self) -> None:
        super().__init__(
            key="core.leaders.goi",
            name=t_("civilization.korea.leaders.goi.name"),
            description=t_("civilization.korea.leaders.goi.description"),
            icon="civilization/korea/leaders/goi/leader_icon.png",
        )
        self._effects = Effects()
