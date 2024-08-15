from openciv.gameplay.leader import Leader
from openciv.gameplay.effect import Effects
from openciv.engine.managers.i18n import _t


class Cnut(Leader):
    def __init__(self):
        super().__init__()
        self.name = _t("civilization.vikings.leaders.cnut.name")
        self.icon = "civilization/vikings/leaders/cnut/leader_icon.png"
        self.description = _t("civilization.vikings.leaders.cnut.description")

        self._effects = Effects()
