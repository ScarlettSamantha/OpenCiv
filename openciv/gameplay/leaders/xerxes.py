from __future__ import annotations

from openciv.gameplay.leader import Leader
from openciv.gameplay.effect import Effects
from openciv.engine.managers.i18n import t_


class Xerxes(Leader):
    def __init__(self) -> None:
        super().__init__(
            key="core.leaders.xerxes",
            name=t_("civilization.persia.leaders.xerxes.name"),
            description=t_("civilization.persia.leaders.xerxes.description"),
            icon="civilization/persia/leaders/xerxes/leader_icon.png",
        )
        self._effects = Effects()
