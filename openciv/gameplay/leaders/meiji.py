from openciv.gameplay.leader import Leader
from openciv.gameplay.effects import Effects
from openciv.engine.managers.i18n import _t


class Meiji(Leader):
    def __init__(self):
        super().__init__()
        self.name = _t("civilization.japan.leaders.meiji.name")
        self.icon = "civilization/japan/leaders/meiji/leader_icon.png"
        self.description = _t("civilization.japan.leaders.meiji.description")

        self._effects = Effects()
