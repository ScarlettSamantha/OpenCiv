from openciv.gameplay.leader import Leader
from openciv.gameplay.effects import Effects
from openciv.engine.managers.i18n import _t


class CharlesIII(Leader):
    def __init__(self):
        super().__init__()
        self.name = _t("civilization.spain.leaders.charles_iii.name")
        self.icon = "civilization/spain/leaders/charles_iii/leader_icon.png"
        self.description = _t("civilization.spain.leaders.charles_iii.description")

        self._effects = Effects()
