from openciv.gameplay.leader import Leader
from openciv.gameplay.effects import Effects
from openciv.engine.managers.i18n import _t


class Charlemagne(Leader):
    def __init__(self):
        super().__init__()
        self.name = _t("civilization.france.leaders.charlemange.name")
        self.icon = "civilization/france/leaders/charlemange/leader_icon.png"
        self.description = _t("civilization.france.leaders.charlemange.description")

        self._effects = Effects()
