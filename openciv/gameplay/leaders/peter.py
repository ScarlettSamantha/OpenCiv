from openciv.gameplay.leader import Leader
from openciv.gameplay.effect import Effects
from openciv.engine.managers.i18n import _t


class Peter(Leader):
    def __init__(self):
        super().__init__()
        self.name = _t("civilization.ussr.leaders.peter.name")
        self.icon = "civilization/ussr/leaders/peter/leader_icon.png"
        self.description = _t("civilization.ussr.leaders.peter.description")

        self._effects = Effects()
