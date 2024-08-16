from openciv.engine.UI.menus.base import Menu
from openciv.engine.managers.game import GameManager


class ModsMenu(Menu):
    def __init__(self, parent: GameManager, onstart: callable):
        Menu.__init__(parent, onstart, 'OpenCiv Mods', False)