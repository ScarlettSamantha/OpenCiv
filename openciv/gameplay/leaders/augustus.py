from openciv.gameplay.leader import Leader
from openciv.gameplay.effect import Effects
from openciv.engine.managers.i18n import _t


class Augustus(Leader):
    def __init__(self):
        super().__init__()
        self.name = _t("civilization.rome.leaders.augustus.name")
        self.icon = "augustus_icon"
        self.description = _t("civilization.rome.leaders.augustus.description")

        self._effects = Effects()
