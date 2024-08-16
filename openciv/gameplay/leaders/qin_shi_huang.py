from __future__ import annotations

from openciv.gameplay.leader import Leader
from openciv.gameplay.effect import Effects
from openciv.engine.managers.i18n import t_


class QinShiHuang(Leader):
    def __init__(self) -> None:
        super().__init__(
            key="core.leaders.qin_shi_huang",
            name=t_("civilization.china.leaders.qin_shi_huang.name"),
            description=t_("civilization.china.leaders.qin_shi_huang.description"),
            icon="civilization/china/leaders/qin_shi_huang/leader_icon.png",
        )
        self._effects = Effects()
