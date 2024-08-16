from openciv.engine.UI.base import BaseUI
from openciv.engine.managers.game import GameManager

from abc import ABC, abstractmethod
from typing import Any


class Menu(BaseUI, ABC):
    def __init__(
            self,
            parent: GameManager,
            onstart: callable,
            title: str,
            popup: bool = False,
            parent_menu: "Menu" = None,
            *args,
            **kwargs):
        BaseUI.__init__(parent, *args, **kwargs)
        self.parent_menu = parent_menu
        self.on_start = onstart
        self.title = title
        self.popup_menu = popup
        self.panel = None
        self._content = None

    @abstractmethod
    def add_content(self):
        pass

    @property
    def content(self) -> "list[Any]":
        return self._content
    
    @content.setter
    def content(self, menu_content: "list[Any]"):
        self._conent = menu_content[:]

    def has_content(self) -> bool:
        return self._content is not None and len(self._content) > 0 

    def render(self):
        if self.has_content():
            self.panel = self.WindowPanel(title=self.title, content=self._content, popup=self.popup_menu)
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
    
