from openciv.gameplay.leader import Leader
from openciv.gameplay.effects import Effects
from openciv.engine.managers.i18n import _t


class WuZetian(Leader):
    def __init__(self):
        super().__init__()
        self.name = _t("civilization.china.leaders.wu_zetian.name")
        self.icon = "civilization/china/leaders/wu_zetian/leader_icon.png"
        self.description = _t("civilization.china.leaders.wu_zetian.description")

        self._effects = Effects()
