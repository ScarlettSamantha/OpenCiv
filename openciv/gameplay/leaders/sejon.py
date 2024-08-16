from __future__ import annotations

from openciv.gameplay.leader import Leader
from openciv.gameplay.effect import Effects
from openciv.engine.managers.i18n import t_


class Sejon(Leader):
    def __init__(self) -> None:
        super().__init__(
            key="core.leaders.sejoin",
            name=t_("civilization.korea.leaders.sejoin.name"),
            description=t_("civilization.korea.leaders.sejoin.description"),
            icon="civilization/korea/leaders/sejoin/leader_icon.png",
        )
        self._effects = Effects()
