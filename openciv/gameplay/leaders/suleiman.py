from openciv.gameplay.leader import Leader
from openciv.gameplay.effects import Effects
from openciv.engine.managers.i18n import _t


class Suleiman(Leader):
    def __init__(self):
        super().__init__()
        self.name = _t("civilization.ottoman.leaders.suleiman.name")
        self.icon = "civilization/ottoman/leaders/suleiman/leader_icon.png"
        self.description = _t("civilization.ottoman.leaders.suleiman.description")

        self._effects = Effects()
