from openciv.gameplay.leader import Leader
from openciv.gameplay.effect import Effects
from openciv.engine.managers.i18n import _t


class Ceasar(Leader):
    def __init__(self):
        super().__init__()
        self.name = _t("civilization.rome.leaders.ceasar.name")
        self.icon = "ceasar_icon"
        self.description = _t("civilization.rome.leaders.ceasar.description")

        self._effects = Effects()
