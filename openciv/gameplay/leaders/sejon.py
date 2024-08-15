from openciv.gameplay.leader import Leader
from openciv.gameplay.effect import Effects
from openciv.engine.managers.i18n import _t


class Sejon(Leader):
    def __init__(self):
        super().__init__()
        self.name = _t("civilization.korea.leaders.sejoin.name")
        self.icon = "civilization/korea/leaders/sejoin/leader_icon.png"
        self.description = _t("civilization.korea.leaders.sejoin.description")

        self._effects = Effects()
