from openciv.gameplay.leader import Leader
from openciv.gameplay.effects import Effects
from openciv.engine.managers.i18n import _t


class Phillip(Leader):
    def __init__(self):
        super().__init__()
        self.name = _t("civilization.spain.leaders.phillip.name")
        self.icon = "civilization/spain/leaders/phillip/leader_icon.png"
        self.description = _t("civilization.spain.leaders.phillip.description")

        self._effects = Effects()
