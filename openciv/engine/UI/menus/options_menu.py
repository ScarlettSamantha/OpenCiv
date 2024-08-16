from openciv.engine.UI.menus.base import Menu
from openciv.engine.managers.game import GameManager


class OptionsMenu(Menu):
    def __init__(self, parent: GameManager, onstart: callable, title: str, popup: bool = False, parent_menu: Menu = None, *args, **kwargs):
        super().__init__(parent, onstart, title, popup, parent_menu, *args, **kwargs)
