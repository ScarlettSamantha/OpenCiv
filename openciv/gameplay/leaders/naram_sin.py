from openciv.gameplay.leader import Leader
from openciv.gameplay.effect import Effects
from openciv.engine.managers.i18n import _t


class NaramSin(Leader):
    def __init__(self):
        super().__init__()
        self.name = _t("civilization.akkadian.leaders.naram_sin.name")
        self.icon = "civilization/akkadian/leaders/naram_sin/leader_icon.png"
        self.description = _t("civilization.akkadian.leaders.naram_sin.description")

        self._effects = Effects()
