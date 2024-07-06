from openciv.engine.managers.game import GameManager
from openciv.gameplay.ui.elements.button import Button as _Button
from openciv.gameplay.ui.elements.text import Text as _Text
from openciv.gameplay.ui.elements.window_panel import WindowPanel as _WindowPanel
from openciv.gameplay.ui.elements.dropdown import DropdownMenu as _DropdownMenu
from openciv.gameplay.ui.elements.dropdown import DropdownMenuButton as _DropdownMenuButton


class BaseUI:
    def __init__(self, parent: GameManager):
        self._parent: GameManager = parent

    def parent(self) -> GameManager:
        return self._parent

    def Button(self, text, click_action=None, *args, **kwargs):
        return _Button(text=text, parent=self.parent, click_action=click_action, *args, **kwargs)

    def Text(self, text, click_action=None, *args, **kwargs):
        return _Text(text=text, parent=self.parent, click_action=click_action, *args, **kwargs)

    def WindowPanel(self, *args, **kwargs):
        return _WindowPanel(*args, **kwargs)

    def DropdownMenu(self, *args, **kwargs):
        return _DropdownMenu(*args, **kwargs)

    def DropdownMenuButton(self, *args, **kwargs):
        return _DropdownMenuButton(*args, **kwargs)

    def get_aspect_ratio(self) -> float:
        from ursina import window

        screen_width = window.fullscreen_size[0]
        screen_height = window.fullscreen_size[1]
        # Calculate aspect ratio
        return screen_width / screen_height
