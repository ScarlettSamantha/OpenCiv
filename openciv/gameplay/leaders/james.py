from openciv.gameplay.leader import Leader
from openciv.gameplay.effect import Effects
from openciv.engine.managers.i18n import _t


class James(Leader):
    def __init__(self):
        super().__init__()
        self.name = _t("civilization.spain.leaders.james.name")
        self.icon = "civilization/spain/leaders/james/leader_icon.png"
        self.description = _t("civilization.spain.leaders.james.description")

        self._effects = Effects()
