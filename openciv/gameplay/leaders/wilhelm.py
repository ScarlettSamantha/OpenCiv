from __future__ import annotations

from openciv.gameplay.leader import Leader
from openciv.gameplay.effect import Effects
from openciv.engine.managers.i18n import t_


class Wilhelm(Leader):
    def __init__(self) -> None:
        super().__init__(
            key="core.leaders.wilhelm",
            name=t_("civilization.germany.leaders.wilhelm.name"),
            description=t_("civilization.germany.leaders.wilhelm.description"),
            icon="civilization/germany/leaders/wilhelm/leader_icon.png",
        )
        self._effects = Effects()
