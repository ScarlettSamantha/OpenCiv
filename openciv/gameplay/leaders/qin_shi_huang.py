from openciv.gameplay.leader import Leader
from openciv.gameplay.effects import Effects
from openciv.engine.managers.i18n import _t


class QinShiHuang(Leader):
    def __init__(self):
        super().__init__()
        self.name = _t("civilization.china.leaders.qin_shi_huang.name")
        self.icon = "civilization/china/leaders/qin_shi_huang/leader_icon.png"
        self.description = _t("civilization.china.leaders.qin_shi_huang.description")

        self._effects = Effects()
