from __future__ import annotations

from openciv.gameplay.leader import Leader
from openciv.gameplay.effect import Effects
from openciv.engine.managers.i18n import t_


class Sargon(Leader):
    def __init__(self) -> None:
        super().__init__(
            key="core.leaders.sargon",
            name=t_("civilization.akkadian.leaders.sargon.name"),
            description=t_("civilization.akkadian.leaders.sargon.description"),
            icon="civilization/akkadian/leaders/sargon/leader_icon.png",
        )
        self._effects = Effects()
