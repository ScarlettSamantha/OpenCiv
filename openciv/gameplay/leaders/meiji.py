from __future__ import annotations

from openciv.gameplay.leader import Leader
from openciv.gameplay.effect import Effects
from openciv.engine.managers.i18n import t_


class Lenin(Leader):
    def __init__(self) -> None:
        super().__init__(
            key="core.leaders.meiji",
            name=t_("civilization.japan.leaders.meiji.name"),
            description=t_("civilization.japan.leaders.meiji.description"),
            icon="civilization/japan/leaders/meiji/leader_icon.png",
        )
        self._effects = Effects()
