from openciv.gameplay.leader import Leader
from openciv.gameplay.effect import Effects
from openciv.engine.managers.i18n import _t


class JoanVanOldenbarnevelt(Leader):
    def __init__(self):
        super().__init__()
        self.name = _t("civilization.low_countries.leaders.joan_van_oldenbarnevelt.name")
        self.icon = "civilization/low_countries/leaders/joan_van_oldenbarnevelt/leader_icon.png"
        self.description = _t("civilization.low_countries.leaders.joan_van_oldenbarnevelt.description")

        self._effects = Effects()
