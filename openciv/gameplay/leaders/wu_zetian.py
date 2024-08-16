from __future__ import annotations

from openciv.gameplay.leader import Leader
from openciv.gameplay.effect import Effects
from openciv.engine.managers.i18n import t_


class WuZetian(Leader):
    def __init__(self) -> None:
        super().__init__(
            key="core.leaders.wu_zetian",
            name=t_("civilization.china.leaders.wu_zetian.name"),
            description=t_("civilization.china.leaders.wu_zetian.description"),
            icon="civilization/china/leaders/wu_zetian/leader_icon.png",
        )
        self._effects = Effects()
