from openciv.gameplay.leader import Leader
from openciv.gameplay.effects import Effects
from openciv.engine.managers.i18n import _t


class Victoria(Leader):
    def __init__(self):
        super().__init__()
        self.name = _t("civilization.england.leaders.victoria.name")
        self.icon = "civilization/england/leaders/victoria/leader_icon.png"
        self.description = _t("civilization.england.leaders.victoria.description")

        self._effects = Effects()
