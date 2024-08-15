from openciv.gameplay.leader import Leader
from openciv.gameplay.effect import Effects
from openciv.engine.managers.i18n import _t


class AbrahamLincoln(Leader):
    def __init__(self):
        super().__init__()
        self.name = _t("civilization.american_empire.leaders.abraham_lincoln.name")
        self.icon = "civilization/american_empire/leaders/abraham_lincoln/leader_icon.png"
        self.description = _t("civilization.american_empire.leaders.abraham_lincoln.description")

        self._effects = Effects()
