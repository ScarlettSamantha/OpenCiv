from openciv.gameplay.leader import Leader
from openciv.gameplay.effect import Effects
from openciv.engine.managers.i18n import _t


class Wilhelm(Leader):
    def __init__(self):
        super().__init__()
        self.name = _t("civilization.germany.leaders.wilhelm.name")
        self.icon = "civilization/germany/leaders/wilhelm/leader_icon.png"
        self.description = _t("civilization.germany.leaders.wilhelm.description")

        self._effects = Effects()
