from __future__ import annotations
from openciv.engine.UI.base import BaseUI
from openciv.engine.UI.menus.base import Menu
from ursina import camera
from openciv.gameplay.ui.elements.button import Button as _Button
from openciv.gameplay.ui.elements.text import Text as _Text
from openciv.gameplay.ui.elements.window_panel import WindowPanel
from openciv.gameplay.ui.elements.listview import ListView


class GameConfig(BaseUI):
    def __init__(self, game_manager, on_back: callable, *args, **kwargs):
        self.panel = None
        self.on_back: callable = on_back
        super().__init__(parent=game_manager, *args, **kwargs)

    def render(self):
        into_text = self.Text("<pre>Configure your game</pre>", size=0.012)
        self.panel = WindowPanel(title="Openciv", popup=False)
        self.panel.enabled = False
        self.panel.layout()
        self.panel.y += 0.4

        content = [
            into_text,
            ListView(
                ["Small", "Medium", "Large", "Huge"],
                parent=camera.ui,
                title="World Size",
                on_change=lambda x: print(x),  # noqa
            ),
            ListView(
                ["Romans", "Egypt", "Large", "Huge"],
                position=(-0.5, 0),
                parent=camera.ui,
                title="Empire",
                on_change=lambda x: print(x),  # noqa
            ),
            self.Button(text="Back", click_action=lambda: self.on_back()),
        ]

        self.panel.content = content

    def Button(self, text, click_action=None, *args, **kwargs):
        return _Button(text=text, parent=self.parent, click_action=click_action, *args, **kwargs)

    def Text(self, text, click_action=None, *args, **kwargs):
        return _Text(text=text, parent=self.parent, click_action=click_action, *args, **kwargs)

    def center(self):
        self.panel.y = self.panel.scale_y / 2 * self.panel.scale_y

    def show(self):
        self.panel.enabled = True

    def hide(self):
        self.panel.enabled = False
        self.panel.disable()
