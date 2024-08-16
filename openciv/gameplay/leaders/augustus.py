from __future__ import annotations

from openciv.gameplay.leader import Leader
from openciv.gameplay.effect import Effects
from openciv.engine.managers.i18n import t_


class Augustus(Leader):
    def __init__(self) -> None:
        super().__init__(
            key="core.leaders.augustus",
            name=t_("civilization.rome.leaders.augustus.name"),
            description=t_("civilization.rome.leaders.augustus.description"),
            icon="civilization/rome/leaders/augustus/leader_icon.png",
        )
        self._effects = Effects()
