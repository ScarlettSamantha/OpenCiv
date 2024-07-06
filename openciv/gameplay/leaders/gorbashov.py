from openciv.gameplay.leader import Leader
from openciv.gameplay.effects import Effects
from openciv.engine.managers.i18n import _t


class Gorbashov(Leader):
    def __init__(self):
        super().__init__()
        self.name = _t("civilization.ussr.leaders.gorbashov.name")
        self.icon = "civilization/ussr/leaders/gorbashov/leader_icon.png"
        self.description = _t("civilization.ussr.leaders.gorbashov.description")

        self._effects = Effects()
