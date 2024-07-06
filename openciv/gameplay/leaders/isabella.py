from openciv.gameplay.leader import Leader
from openciv.gameplay.effects import Effects
from openciv.engine.managers.i18n import _t


class Isabella(Leader):
    def __init__(self):
        super().__init__()
        self.name = _t("civilization.spain.leaders.isabella.name")
        self.icon = "civilization/spain/leaders/isabella/leader_icon.png"
        self.description = _t("civilization.spain.leaders.isabella.description")

        self._effects = Effects()
