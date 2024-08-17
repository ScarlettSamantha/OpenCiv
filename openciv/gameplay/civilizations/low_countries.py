from __future__ import annotations

from openciv.gameplay.civilization import Civilization
from openciv.engine.managers.i18n import t_


class LowCountries(Civilization):
    def __init__(self) -> None:
        super().__init__(
            name=t_("civilization.low_countries.name"), description=t_("civilization.low_countries.description")
        )

        self._loadable = True
        self.icon = "icons/rome.png"

    def register_effects(self) -> None:
        pass

    def register_leaders(self) -> None:
        from openciv.gameplay.leaders.willem import Willem
        from openciv.gameplay.leaders.ambiorix import Ambiorix

        self.add_leader(leader=Willem())
        self.add_leader(leader=Ambiorix())
