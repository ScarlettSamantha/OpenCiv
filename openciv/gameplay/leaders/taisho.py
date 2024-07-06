from openciv.gameplay.leader import Leader
from openciv.gameplay.effects import Effects
from openciv.engine.managers.i18n import _t


class Taisho(Leader):
    def __init__(self):
        super().__init__()
        self.name = _t("civilization.japan.leaders.taisho.name")
        self.icon = "civilization/japan/leaders/taisho/leader_icon.png"
        self.description = _t("civilization.japan.leaders.taisho.description")

        self._effects = Effects()
