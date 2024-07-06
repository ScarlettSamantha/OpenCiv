from openciv.gameplay.leader import Leader
from openciv.gameplay.effects import Effects
from openciv.engine.managers.i18n import _t


class Goi(Leader):
    def __init__(self):
        super().__init__()
        self.name = _t("civilization.korea.leaders.goi.name")
        self.icon = "civilization/korea/leaders/goi/leader_icon.png"
        self.description = _t("civilization.korea.leaders.goi.description")

        self._effects = Effects()
