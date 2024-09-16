from __future__ import annotations
from typing import Any
from openciv.engine.managers.base import BaseSingletonManager
from openciv.engine.UI import V
from openciv.engine.UI.menus.main_menu import MainMenu


class UIManager(BaseSingletonManager):
    
    def __setup__(self) -> None:
        self.current_view: V = None
        self.previous_view: V = None

    def __call__(self, **kwargs: Any) -> Any:
        self.__setup__(**kwargs)
        return self

    def start(self):
        """
        Game boots into the main menu, so first thing after __init__ is to instantiate and set the
        initial active view to the main menu.
        """
        self.current_view = MainMenu(self.parent())
        self.activate_current_view()

    def shutdown_previous_view(self):
        self.previous_view.hide()
        self.previous_view.clear()

    def activate_current_view(self):
        if not isinstance(self.current_view, V.__constraints__):
            view_cls = self.current_view
            self.current_view = view_cls(self.parent())

        if self.current_view is not None and isinstance(self.current_view, V.__constraints__):
            menu_elems = self.current_view.setup_content()
            self.parent().log().engine.debug(f'view class: {self.current_view.__class__} preparing to render...')
            self.parent().log().engine.debug(f'view content created: {menu_elems}')
            self.current_view.populate(menu_elems)
            self.current_view.render()
            self.current_view.show()
        else:
            self.parent().log().engine.debug(f'unable to instantiate view of type: {view_cls}')

    def revert_view(self):
        self.change_to_menu(self.previous_view)

    def change_to_tab(self):
        pass

    def change_to_menu(self, menu: V):
        self.previous_view = self.current_view
        self.current_view = menu
        self.shutdown_previous_view()
        self.activate_current_view()
