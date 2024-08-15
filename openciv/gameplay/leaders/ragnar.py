from openciv.gameplay.leader import Leader
from openciv.gameplay.effect import Effects
from openciv.engine.managers.i18n import _t


class Ragnar(Leader):
    def __init__(self):
        super().__init__()
        self.name = _t("civilization.vikings.leaders.ragnar.name")
        self.icon = "civilization/vikings/leaders/ragnar/leader_icon.png"
        self.description = _t("civilization.vikings.leaders.ragnar.description")

        self._effects = Effects()
