from openciv.gameplay.leader import Leader
from openciv.gameplay.effect import Effects
from openciv.engine.managers.i18n import _t


class Leonidas(Leader):
    def __init__(self):
        super().__init__()
        self.name = _t("civilization.greece.leaders.leonidas.name")
        self.icon = "civilization/greece/leaders/leonidas/leader_icon.png"
        self.description = _t("civilization.greece.leaders.leonidas.description")

        self._effects = Effects()
