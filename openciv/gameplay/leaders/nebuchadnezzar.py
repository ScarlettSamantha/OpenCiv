from openciv.gameplay.leader import Leader
from openciv.gameplay.effects import Effects
from openciv.engine.managers.i18n import _t


class Nebuchadnezzar(Leader):
    def __init__(self):
        super().__init__()
        self.name = _t("civilization.persia.leaders.nebuchadnezzar.name")
        self.icon = "civilization/persia/leaders/nebuchadnezzar/leader_icon.png"
        self.description = _t("civilization.persia.leaders.nebuchadnezzar.description")

        self._effects = Effects()
