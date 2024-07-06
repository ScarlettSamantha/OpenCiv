from openciv.engine.UI.base import BaseUI
from ursina import camera, color, window
from openciv.engine.entity import Entity


class TestMenu(BaseUI):
    def __init__(self, game_manager, call: callable, *args, **kwargs):
        self.panel = None
        self.on_start: callable = call
        super().__init__(parent=game_manager, *args, **kwargs)

    def render(self):
        ent = Entity(
            model="quad",
            color=color.black,
            position=window.top_left,
            scale=(self.get_aspect_ratio() / 2, 1),
            z=1,
            origin=(-0.5, 0.5),
            collider="box",
            parent=camera.ui,
        )
        ent.enabled = True

    def center(self):
        self.panel.y = self.panel.scale_y / 2 * self.panel.scale_y

    def show(self):
        pass

    def hide(self):
        pass
