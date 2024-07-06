from openciv.gameplay.leader import Leader
from openciv.gameplay.effects import Effects
from openciv.engine.managers.i18n import _t


class Ambiorix(Leader):
    def __init__(self):
        super().__init__()
        self.name = _t("civilization.low_countries.leaders.ambiorix.name")
        self.icon = "civilization/low_countries/leaders/ambiorix/leader_icon.png"
        self.description = _t("civilization.low_countries.leaders.ambiorix.description")

        self._effects = Effects()
