from openciv.engine.UI.base import BaseUI

from abc import ABC, abstractmethod
from typing import Any
from ursina import destroy

class Menu(BaseUI, ABC):
    """
    Base class for all game menus.
    """
    def __init__(
            self,
            parent,
            title: str,
            popup: bool = False,
            *args,
            **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.title = title
        self.popup_menu = popup
        self.panel = None
        self._content = None

    @abstractmethod
    def setup_content(self) -> "list[Any]":
        pass

    def get_reachable_menus(self) -> "list[Menu]":
        """
        Returns a list of all other menus or views, children or otherwise, that can be navigated to
        from this current menu.
        """
        nav_buttons = list(filter(lambda elem: hasattr(elem, 'destination'), self._content))
        return [getattr(nav, 'destination') for nav in nav_buttons]
    
    def has_content(self) -> bool:
        return self._content is not None and len(self._content) > 0
    
    def populate(self, menu_content: "list[Any]") -> None:
        self._content = menu_content[:]

    def render(self):
        if self.has_content():
            self.panel = self.WindowPanel(title=self.title, content=self._content, popup=self.popup_menu, )
            self.center()
            self.panel.enabled = False
            self.panel.layout()
            self.panel.y += 0.4

    def center(self):
        self.panel.y = self.panel.scale_y / 2 * self.panel.scale_y

    def show(self):
        self.panel.enabled = True

    def hide(self):
        self.panel.enabled = False

    def clear(self):
        for c in self._content:
            destroy(c)


class SubMenu(Menu, ABC):
    """
    Base class for general sub-menus.
    """
    def __init__(
            self,
            parent_menu: Menu,
            title: str,
            *args, **kwargs):
        super().__init__(parent_menu.parent(), title, popup=False, *args, **kwargs)
        self.parent_menu = parent_menu

    @abstractmethod
    def setup_content(self):
        pass

    @property
    def tab_name(self) -> str:
        return self.title


class TabbedMenu(Menu, ABC):
    """
    A more specific menu base class for a menu that <em>must</em> have 
    child submenus, which are displayed as different tabs.

    Currently, just renders some placeholder stuff.
    """
    def __init__(
            self,
            parent,
            title: str,
            *args,
            **kwargs):
        super().__init__(parent=parent, title=title, popup=False, *args, **kwargs)
        # self.submenu_tabs: tuple[SubMenu] = None

    @abstractmethod
    def get_submenu_tabs(self) -> "tuple[SubMenu]":
        pass

    @abstractmethod
    def get_submenu_names(self) -> "tuple[str]":
        pass

    @abstractmethod
    def setup_content(self):
        pass