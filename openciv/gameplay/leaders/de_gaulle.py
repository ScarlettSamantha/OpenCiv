from openciv.gameplay.leader import Leader
from openciv.gameplay.effects import Effects
from openciv.engine.managers.i18n import _t


class DeGaulle(Leader):
    def __init__(self):
        super().__init__()
        self.name = _t("civilization.france.leaders.de_gaulle.name")
        self.icon = "civilization/france/leaders/de_gaulle/leader_icon.png"
        self.description = _t("civilization.france.leaders.de_gaulle.description")

        self._effects = Effects()
