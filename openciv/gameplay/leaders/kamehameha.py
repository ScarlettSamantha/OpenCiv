from openciv.gameplay.leader import Leader
from openciv.gameplay.effects import Effects
from openciv.engine.managers.i18n import _t


class Kamehameha(Leader):
    def __init__(self):
        super().__init__()
        self.name = _t("civilization.american_empire.leaders.kamehameha.name")
        self.icon = "civilization/american_empire/leaders/kamehameha/leader_icon.png"
        self.description = _t("civilization.american_empire.leaders.kamehameha.description")

        self._effects = Effects()
