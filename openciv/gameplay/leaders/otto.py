from openciv.gameplay.leader import Leader
from openciv.gameplay.effect import Effects
from openciv.engine.managers.i18n import _t


class Otto(Leader):
    def __init__(self):
        super().__init__()
        self.name = _t("civilization.germany.leaders.otto.name")
        self.icon = "civilization/germany/leaders/otto/leader_icon.png"
        self.description = _t("civilization.germany.leaders.otto.description")

        self._effects = Effects()
