from __future__ import annotations
from openciv.engine.managers.base import BaseManager
from openciv.engine.UI.menus import *


class UIManager(BaseManager):
    def __init__(self):
        self.active_menu = None
        self.previous_menu = None
        self.menus = []

        # TODO remove after finishing refactor...
        self.main_menu = None
        self.game_config = None
        self.test_menu = None

    def _add_available_menus(self):
        pass

    def change_to_menu(self, menu: Menu):
        self.previous_menu = self.active_menu
        self.active_menu = menu

    def activate_current_menu(self):
        self.active_menu.render()
        self.active_menu.show()

    def start_test_menu(self):
        

        self.stop_main_menu()

        if self.test_menu is None:
            self.test_menu = TestMenu(self.parent, self.start_main_menu)
            self.test_menu.render()
            self.test_menu.show()

    def stop_test_menu(self):
        if self.test_menu is not None:
            self.test_menu.hide()
            self.test_menu = None

    def is_test_menu_open(self) -> bool:
        return self.test_menu.enabled

    def start_main_menu(self):
        

        self.stop_game_config()

        if self.main_menu is None:
            self.main_menu = MainMenu(self.parent, self.start_game_config)
            self.main_menu.render()
            self.main_menu.show()

    def stop_main_menu(self):
        if self.main_menu is not None:
            self.main_menu.hide()
            self.main_menu = None

    def is_main_menu_open(self) -> bool:
        return self.main_menu.enabled

    def start_game_config(self):
        

        self.stop_main_menu()

        if self.game_config is None:
            self.game_config = GameConfig(self.parent, self.start_main_menu)
            self.game_config.render()
            self.game_config.show()

    def stop_game_config(self):
        if self.game_config is not None:
            self.game_config.hide()
            self.game_config = None

    def is_game_config_open(self) -> bool:
        return self.game_config.enabled
