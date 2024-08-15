from openciv.gameplay.leader import Leader
from openciv.gameplay.effect import Effects
from openciv.engine.managers.i18n import _t


class Justinian(Leader):
    def __init__(self):
        super().__init__()
        self.name = _t("civilization.byzantine.leaders.justinian.name")
        self.icon = "civilization/byzantine/leaders/justinian/leader_icon.png"
        self.description = _t("civilization.byzantine.leaders.justinian.description")

        self._effects = Effects()
