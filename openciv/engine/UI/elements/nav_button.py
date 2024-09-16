from __future__ import annotations
from openciv.engine.UI.elements.button import Button

class NavButton(Button):
    def __init__(self, parent, dest, *args, **kwargs):
        # TODO: store reference to menu the button is on?
        self._destination_view = dest
        self._parent_manager = parent
        super().__init__(*args, parent=parent, click_action=self._navigate_onclick_action, **kwargs)

    def _navigate_onclick_action(self):
        self._parent_manager.ui().change_to_menu(self._destination_view)

    @property
    def destination(self):
        return self._destination_view