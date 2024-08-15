from openciv.gameplay.leader import Leader
from openciv.gameplay.effect import Effects
from openciv.engine.managers.i18n import _t


class Cleopatra(Leader):
    def __init__(self):
        super().__init__()
        self.name = _t("civilization.egypte.leaders.cleopatra.name")
        self.icon = "civilization/egypte/leaders/cleopatra/leader_icon.png"
        self.description = _t("civilization.egypte.leaders.cleopatra.description")

        self._effects = Effects()
