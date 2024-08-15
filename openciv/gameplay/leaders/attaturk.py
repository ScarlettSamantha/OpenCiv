from openciv.gameplay.leader import Leader
from openciv.gameplay.effect import Effects
from openciv.engine.managers.i18n import _t


class Attaturk(Leader):
    def __init__(self):
        super().__init__()
        self.name = _t("civilization.ottoman.leaders.attaturk.name")
        self.icon = "civilization/ottoman/leaders/attaturk/leader_icon.png"
        self.description = _t("civilization.ottoman.leaders.attaturk.description")

        self._effects = Effects()
