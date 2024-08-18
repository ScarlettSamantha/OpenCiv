from __future__ import annotations
from ursina import Text as _text
from typing import Callable

class Text(_text):
    def __init__(self, parent, click_action: Callable = None, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.click_action = click_action
        self._parent = parent

    def trigger_click_action(self):
        if self.click_action is not None:
            self.click_action()
