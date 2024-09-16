from __future__ import annotations
# from openciv.engine.managers.ui import UIManager
from openciv.engine.UI.elements.button import Button as _Button
from openciv.engine.UI.elements.nav_button import NavButton as _NavButton
from openciv.engine.UI.elements.link_button import LinkButton as _LinkButton
from openciv.engine.UI.elements.text import Text as _Text
from openciv.engine.UI.elements.window_panel import WindowPanel as _WindowPanel
from openciv.engine.UI.elements.dropdown import DropdownMenu as _DropdownMenu
from openciv.engine.UI.elements.dropdown import DropdownMenuButton as _DropdownMenuButton
from openciv.engine.UI.elements.tabbed_panel import TabbedPanel as _TabbedPanel
from openciv.engine.UI.elements.tab_button import TabButton as _TabButton
from openciv.engine.UI.elements.tab_group import TabGroup as _TabGroup
from openciv.engine.UI.elements.listview import ListView as _ListView


class BaseUI:
    def __init__(self, parent):
        self._parent = parent

    def parent(self):
        return self._parent

    def Button(self, text: str, click_action=None, radius=0.0, *args, **kwargs):
        return _Button(text=text, parent=self.parent, click_action=click_action,
                       radius=radius, *args, **kwargs)
    
    def NavButton(self, text: str, destination, *args, **kwargs):
        return _NavButton(text=text, radius=0.0, parent=self.parent(), dest=destination, *args, **kwargs)
    
    def BackButton(self):
        return _Button(text='Back', parent=self.parent, click_action=self.parent().ui().revert_view)
        
    def LinkButton(self, text:str, url: str):
        return _LinkButton(parent=self.parent, text=text, url=url)

    def Text(self, text: str, click_action=None, *args, **kwargs):
        return _Text(text=text, parent=self.parent, click_action=click_action, *args, **kwargs)

    def WindowPanel(self, *args, **kwargs):
        return _WindowPanel(*args, **kwargs)
    
    def TabbedPanel(self, *args, **kwargs):
        return _TabbedPanel(*args, **kwargs)
    
    def TabButton(self, *args, **kwargs):
        return _TabButton(*args, **kwargs)
    
    def TabGroup(self, tabbed_menu, *args, **kwargs):
        return _TabGroup(parent_menu=tabbed_menu, *args, **kwargs)

    def DropdownMenu(self, *args, **kwargs):
        return _DropdownMenu(*args, **kwargs)

    def DropdownMenuButton(self, *args, **kwargs):
        return _DropdownMenuButton(*args, **kwargs)
    
    def ListView(self, items, on_change: callable, title: str = "", **kwargs):
        return _ListView(items, on_change, title, **kwargs)

    def get_aspect_ratio(self) -> float:
        from ursina import window

        screen_width = window.fullscreen_size[0]
        screen_height = window.fullscreen_size[1]
        # Calculate aspect ratio
        return screen_width / screen_height
