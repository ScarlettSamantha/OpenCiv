from openciv.gameplay.leader import Leader
from openciv.gameplay.effect import Effects
from openciv.engine.managers.i18n import _t


class CharlesV(Leader):
    def __init__(self):
        super().__init__()
        self.name = _t("civilization.spain.leaders.charles_v.name")
        self.icon = "civilization/spain/leaders/charles_v/leader_icon.png"
        self.description = _t("civilization.spain.leaders.charles_v.description")

        self._effects = Effects()
