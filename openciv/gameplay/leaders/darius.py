from openciv.gameplay.leader import Leader
from openciv.gameplay.effect import Effects
from openciv.engine.managers.i18n import _t


class Darius(Leader):
    def __init__(self):
        super().__init__()
        self.name = _t("civilization.persia.leaders.darius.name")
        self.icon = "civilization/persia/leaders/darius/leader_icon.png"
        self.description = _t("civilization.persia.leaders.darius.description")

        self._effects = Effects()
