from openciv.gameplay.leader import Leader
from openciv.gameplay.effects import Effects
from openciv.engine.managers.i18n import _t


class Constantine(Leader):
    def __init__(self):
        super().__init__()
        self.name = _t("civilization.byzantine.leaders.constantine.name")
        self.icon = "civilization/byzantine/leaders/constantine/leader_icon.png"
        self.description = _t("civilization.byzantine.leaders.constantine.description")

        self._effects = Effects()
