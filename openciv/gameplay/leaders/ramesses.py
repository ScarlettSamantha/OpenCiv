from __future__ import annotations

from openciv.gameplay.leader import Leader
from openciv.gameplay.effect import Effects
from openciv.engine.managers.i18n import t_


class Ramesses(Leader):
    def __init__(self) -> None:
        super().__init__(
            key="core.leaders.ramesses",
            name=t_("civilization.egypte.leaders.ramesses.name"),
            description=t_("civilization.egypte.leaders.ramesses.description"),
            icon="civilization/egypte/leaders/ramesses/leader_icon.png",
        )
        self._effects = Effects()
