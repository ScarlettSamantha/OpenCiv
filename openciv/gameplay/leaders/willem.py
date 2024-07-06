from openciv.gameplay.leader import Leader
from openciv.gameplay.effects import Effects
from openciv.engine.managers.i18n import _t


class Willem(Leader):
    def __init__(self):
        super().__init__()
        self.name = _t("civilization.low_countries.leaders.willem.name")
        self.icon = "civilization/low_countries/leaders/willem/leader_icon.png"
        self.description = _t("civilization.low_countries.leaders.willem.description")

        self._effects = Effects()
