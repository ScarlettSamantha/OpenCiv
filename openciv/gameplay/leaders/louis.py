from __future__ import annotations

from openciv.gameplay.leader import Leader
from openciv.gameplay.effect import Effects
from openciv.engine.managers.i18n import t_


class Lenin(Leader):
    def __init__(self) -> None:
        super().__init__(
            key="core.leaders.louis",
            name=t_("civilization.france.leaders.louis.name"),
            description=t_("civilization.france.leaders.louis.description"),
            icon="civilization/france/leaders/louis/leader_icon.png",
        )
        self._effects = Effects()
