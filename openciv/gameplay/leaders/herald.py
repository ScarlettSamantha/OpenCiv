from openciv.gameplay.leader import Leader
from openciv.gameplay.effects import Effects
from openciv.engine.managers.i18n import _t


class Herald(Leader):
    def __init__(self):
        super().__init__()
        self.name = _t("civilization.vikings.leaders.herald.name")
        self.icon = "civilization/vikings/leaders/herald/leader_icon.png"
        self.description = _t("civilization.vikings.leaders.herald.description")

        self._effects = Effects()
