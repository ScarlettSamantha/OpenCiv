from openciv.gameplay.leader import Leader
from openciv.gameplay.effect import Effects
from openciv.engine.managers.i18n import _t


class SittingBull(Leader):
    def __init__(self):
        super().__init__()
        self.name = _t("civilization.american_empire.leaders.sitting_bull.name")
        self.icon = "civilization/american_empire/leaders/sitting_bull/leader_icon.png"
        self.description = _t("civilization.american_empire.leaders.sitting_bull.description")

        self._effects = Effects()
