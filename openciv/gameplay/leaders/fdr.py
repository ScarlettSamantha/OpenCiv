from openciv.gameplay.leader import Leader
from openciv.gameplay.effect import Effects
from openciv.engine.managers.i18n import _t


class FDR(Leader):
    def __init__(self):
        super().__init__()
        self.name = _t("civilization.american_empire.leaders.fdr.name")
        self.icon = "civilization/american_empire/leaders/fdr/leader_icon.png"
        self.description = _t("civilization.american_empire.leaders.fdr.description")

        self._effects = Effects()
