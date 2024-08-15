from openciv.gameplay.leader import Leader
from openciv.gameplay.effect import Effects
from openciv.engine.managers.i18n import _t


class Tokugawa(Leader):
    def __init__(self):
        super().__init__()
        self.name = _t("civilization.japan.leaders.tokugawa.name")
        self.icon = "civilization/japan/leaders/tokugawa/leader_icon.png"
        self.description = _t("civilization.japan.leaders.tokugawa.description")

        self._effects = Effects()
