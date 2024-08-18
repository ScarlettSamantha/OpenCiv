from __future__ import annotations
from ursina.prefabs.dropdown_menu import DropdownMenu as _DropdownMenu
from ursina.prefabs.dropdown_menu import DropdownMenuButton as _DropdownMenuButton


class DropdownMenuButton(_DropdownMenuButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class DropdownMenu(_DropdownMenu):
    def __init__(self, text, buttons, *args, **kwargs):
        super().__init__(text=text, buttons=buttons, *args, **kwargs)
