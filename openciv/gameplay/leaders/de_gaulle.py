from __future__ import annotations

from openciv.gameplay.leader import Leader
from openciv.gameplay.effect import Effects
from openciv.engine.managers.i18n import t_


class DeGaulle(Leader):
    def __init__(self) -> None:
        super().__init__(
            key="core.leaders.de_gaulle",
            name=t_("civilization.france.leaders.de_gaulle.name"),
            description=t_("civilization.france.leaders.de_gaulle.description"),
            icon="civilization/france/leaders/de_gaulle/leader_icon.png",
        )
        self._effects = Effects()
