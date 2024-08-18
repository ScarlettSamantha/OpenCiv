from __future__ import annotations
from ursina import Entity as _BaseEntity


class Entity(_BaseEntity):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def get_ui_camera(self):
        from ursina import camera

        return camera.ui_camera
