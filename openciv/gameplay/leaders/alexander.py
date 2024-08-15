from openciv.gameplay.leader import Leader
from openciv.gameplay.effect import Effects
from openciv.engine.managers.i18n import _t


class Alexander(Leader):
    def __init__(self):
        super().__init__()
        self.name = _t("civilization.greece.leaders.alexander.name")
        self.icon = "civilization/greece/leaders/alexander/leader_icon.png"
        self.description = _t("civilization.greece.leaders.alexander.description")

        self._effects = Effects()
