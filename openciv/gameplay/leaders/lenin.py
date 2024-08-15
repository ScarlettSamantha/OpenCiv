from openciv.gameplay.leader import Leader
from openciv.gameplay.effect import Effects
from openciv.engine.managers.i18n import _t


class Lenin(Leader):
    def __init__(self):
        super().__init__()
        self.name = _t("civilization.ussr.leaders.lenin.name")
        self.icon = "civilization/ussr/leaders/lenin/leader_icon.png"
        self.description = _t("civilization.ussr.leaders.lenin.description")

        self._effects = Effects()
