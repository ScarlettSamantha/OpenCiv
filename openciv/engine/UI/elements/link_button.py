from __future__ import annotations
import webbrowser
from typing import Callable
from openciv.engine.UI.elements.button import Button


class LinkButton(Button):
    """
    A button subclass which opens an external web hyperlink.
    """
    def __init__(self, parent, url=None, *args, **kwargs):
        self._url = url
        super().__init__(parent, *args, **kwargs)

    def trigger_click_action(self):
        if self._url is not None and len(self._url) > 0:
            webbrowser.open_new(self._url)