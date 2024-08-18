from __future__ import annotations
from openciv.gameplay.techs.trees.core import Core
from openciv.engine.managers.i18n import set_i18n, _i18n

if __name__ == "__main__":
    set_i18n(_i18n("openciv/i18n/en_EN.json"))
    Core().render()
