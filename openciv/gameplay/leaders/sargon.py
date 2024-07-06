from openciv.gameplay.leader import Leader
from openciv.gameplay.effects import Effects
from openciv.engine.managers.i18n import _t


class Sargon(Leader):
    def __init__(self):
        super().__init__()
        self.name = _t("civilization.akkadian.leaders.sargon.name")
        self.icon = "civilization/akkadian/leaders/sargon/leader_icon.png"
        self.description = _t("civilization.akkadian.leaders.sargon.description")

        self._effects = Effects()
