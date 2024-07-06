from openciv.gameplay.leader import Leader
from openciv.gameplay.effects import Effects
from openciv.engine.managers.i18n import _t


class Ramesses(Leader):
    def __init__(self):
        super().__init__()
        self.name = _t("civilization.egypte.leaders.ramesses.name")
        self.icon = "civilization/egypte/leaders/ramesses/leader_icon.png"
        self.description = _t("civilization.egypte.leaders.ramesses.description")

        self._effects = Effects()
