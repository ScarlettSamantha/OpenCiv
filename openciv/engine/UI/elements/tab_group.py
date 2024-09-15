from __future__ import annotations
# from ursina import entity, Text, Button, ButtonList, destroy
from ursina.prefabs.button_group import ButtonGroup
from ursina.scripts.grid_layout import grid_layout

from openciv.engine.UI.elements.tab_button import TabButton
from openciv.engine.managers.log import LogManager


class TabGroup(ButtonGroup):
    """
    A specialized ButtonGroup (which is a set of mutually exclusive buttons, displayed
    horizontally) that stores the tabs corresponding to each submenu within a tabbed panel/menu.
    """
    def __init__(self, parent_menu, **kwargs) -> None:
        self._tab_submenu_instances = [tabcls(parent_menu=parent_menu) for tabcls in parent_menu.get_submenu_tabs()] 
        self._tab_options_dict = {tab_inst.tab_name: tab_inst for tab_inst in self._tab_submenu_instances }
        super().__init__(options=self._tab_options_dict.keys(), min_selection=1, max_selection=1, **kwargs)

    def on_value_changed(self):
        """
        TODO implement to customize what happens when one of the button options is selected
        """
        LogManager.get_instance().engine.debug(f'Tab group value changed to: {self.value}')
        print(self.value)
        