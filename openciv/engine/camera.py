from __future__ import annotations
from ursina import camera, Vec2, Entity, Vec3, mouse, held_keys, lerp, slerp, time, destroy, curve

from openciv.engine.managers.game import GameManager
from openciv.engine import ui
from openciv.gameplay.ui.elements.button import Button


class Camera(Entity):
    def __init__(self, game_manager: GameManager = None, **kwargs):
        camera.editor_position = camera.position
        super().__init__(name="camera", eternal=False)

        self.game_manager: GameManager = game_manager
        self.rotation_speed = 200
        self.pan_speed = Vec2(7, 7)
        self.move_speed = 10
        self.speed_modifier = 1.0  # Speed modifier property
        self.target_fov = 75
        self.zoom_speed = 1.25
        self.zoom_smoothing = 8
        self.rotate_around_mouse_hit = False
        self.ignore_scroll_on_ui = True

        self.smoothing_helper = Entity(add_to_scene_entities=False)
        self.rotation_smoothing = 0
        self.look_at = self.smoothing_helper.look_at
        self.look_at_2d = self.smoothing_helper.look_at_2d
        self.rotate_key = "right mouse"

        for key, value in kwargs.items():
            setattr(self, key, value)

        self.start_position = self.position
        self.default_position = Vec3(12, 8, -3)  # Default position property
        self.default_rotation = Vec3(40, 0, 0)  # Default rotation property
        self.default_scale = Vec3(1.5, 1.5, 1.5)  # Default zoom level
        self.perspective_fov = camera.fov
        self.on_destroy = self.on_disable
        self.shortcuts = {"focus": "shift+f", "reset_center": "alt+f"}

        self.ui = ui.UI()

        self.game_world_interactive = True

    def gameInteractive(self, state: bool):
        self.game_world_interactive = state

    def on_enable(self):
        self.org_cam_par = camera.parent
        self.org_cam_pos = camera.position
        self.org_cam_rot = camera.rotation
        camera.parent = self
        camera.position = camera.editor_position
        camera.rotation = (0, 0, 0)
        self.target_z = camera.z
        self.target_fov = camera.fov

        self.to_default_position()

    def save_map(self):
        from openciv.engine.saving import Saving

        saving_instance = Saving()
        saving_instance.toJson(self.grid_ref)

    def handle_click(self):
        # Convert the mouse position to world coordinates
        clicked_tile = mouse.hovered_entity
        if self.game_world_interactive:
            if clicked_tile is not None:
                self.ui.mainWindow(clicked_tile)
        self.ui_element_triggers(clicked_tile=clicked_tile)

    def ui_element_triggers(self, clicked_tile):
        if clicked_tile is not None and isinstance(clicked_tile, Button) and hasattr(clicked_tile, "click_action"):
            clicked_tile.trigger_click_action()

    def on_disable(self):
        camera.editor_position = camera.position
        if hasattr(self, "org_cam_par"):
            camera.parent = self.org_cam_par
            camera.position = self.org_cam_pos
            camera.rotation = self.org_cam_rot

    def on_destroy(self):
        destroy(self.smoothing_helper)

    def to_default_position(self):
        self.animate_position(self.default_position, 3)
        self.animate_rotation(self.default_rotation, 3)
        self.animate_scale(self.default_scale)

    def input(self, key):
        combined_key = "".join(e + "+" for e in ("control", "shift", "alt") if held_keys[e] and not e == key) + key

        if combined_key == self.shortcuts["reset_center"]:
            self.to_default_position()

        elif key == "y":
            self.gameInteractive(not self.game_world_interactive)

        elif key == "l":
            self.game_manager.ui().start_main_menu()

        elif key == "left mouse down":
            self.handle_click()

        elif key == "i":
            self.save_map()

        elif key == "z":
            self.ui.panel.enable()

        elif combined_key == self.shortcuts["focus"] and mouse.world_point:
            self.animate_position(mouse.world_point, duration=0.1, curve=curve.linear)

        elif key == "scroll up" and self.game_world_interactive:
            if self.ignore_scroll_on_ui and mouse.hovered_entity and mouse.hovered_entity.has_ancestor(camera.ui):
                return
            self.target_z += self.zoom_speed * (abs(self.target_z) * 0.1)

        elif key == "scroll down" and self.game_world_interactive:
            if self.ignore_scroll_on_ui and mouse.hovered_entity and mouse.hovered_entity.has_ancestor(camera.ui):
                return
            self.target_z -= self.zoom_speed * (abs(self.target_z) * 0.1)

        elif (key == "right mouse down" or key == "middle mouse down") and self.game_world_interactive:
            if mouse.hovered_entity and self.rotate_around_mouse_hit:
                org_pos = camera.world_position
                self.world_position = mouse.world_point
                camera.world_position = org_pos

        elif key == "c":  # Dump camera properties to CLI
            self.dump_camera_properties()

    def dump_camera_properties(self):
        print(f"Camera Position: {self.position}")  # noqa
        print(f"Camera Rotation: {self.rotation}")  # noqa
        print(f"Camera Scale: {self.scale}")  # noqa

    def goto(self, position: Vec3, rotation: Vec3 = None):
        self.position = position
        camera.position = position
        if rotation:
            self.rotation = rotation
            camera.rotation = rotation

    def update(self):
        if held_keys["gamepad right stick y"] or held_keys["gamepad right stick x"]:
            self.smoothing_helper.rotation_x -= held_keys["gamepad right stick y"] * self.rotation_speed / 100
            self.smoothing_helper.rotation_y += held_keys["gamepad right stick x"] * self.rotation_speed / 100

        move_speed = self.move_speed * self.speed_modifier  # Apply speed modifier

        if self.game_world_interactive:
            if held_keys["w"]:
                self.position += camera.up * move_speed * time.dt
                self.position += camera.forward * move_speed * time.dt

            elif held_keys["s"]:
                self.position -= camera.up * move_speed * time.dt
                self.position -= camera.forward * move_speed * time.dt

            elif held_keys["a"]:
                self.position -= camera.right * move_speed * time.dt

            elif held_keys["d"]:
                self.position += camera.right * move_speed * time.dt

            elif held_keys[self.rotate_key]:
                self.smoothing_helper.rotation_x -= mouse.velocity[1] * self.rotation_speed
                self.smoothing_helper.rotation_y += mouse.velocity[0] * self.rotation_speed

                self.direction = Vec3(
                    self.forward * (held_keys["w"] - held_keys["s"])
                    + self.right * (held_keys["d"] - held_keys["a"])
                    + self.up * (held_keys["e"] - held_keys["q"])
                ).normalized()

                self.position += (
                    self.direction
                    * (move_speed + (move_speed * held_keys["shift"]) - (move_speed * 0.9 * held_keys["alt"]))
                    * time.dt
                )

                if self.target_z < 0:
                    self.target_z += (
                        held_keys["w"]
                        * (move_speed + (move_speed * held_keys["shift"]) - (move_speed * 0.9 * held_keys["alt"]))
                        * time.dt
                    )
                else:
                    self.position += (
                        camera.forward
                        * held_keys["w"]
                        * (move_speed + (move_speed * held_keys["shift"]) - (move_speed * 0.9 * held_keys["alt"]))
                        * time.dt
                    )

                self.target_z -= (
                    held_keys["s"]
                    * (move_speed + (move_speed * held_keys["shift"]) - (move_speed * 0.9 * held_keys["alt"]))
                    * time.dt
                )

            if mouse.middle:
                zoom_compensation = -self.target_z * 0.1

                self.position -= camera.right * mouse.velocity[0] * self.pan_speed[0] * zoom_compensation
                self.position -= camera.up * mouse.velocity[1] * self.pan_speed[1] * zoom_compensation

            camera.z = lerp(camera.z, self.target_z, time.dt * self.zoom_smoothing)

            if self.rotation_smoothing == 0:
                self.rotation = self.smoothing_helper.rotation
            else:
                self.quaternion = slerp(
                    self.quaternion, self.smoothing_helper.quaternion, time.dt * self.rotation_smoothing
                )
                camera.world_rotation_z = 0

    def __setattr__(self, name, value):
        super().__setattr__(name, value)
        if hasattr(self, "smoothing_helper") and name in ("rotation", "rotation_x", "rotation_y", "rotation_z"):
            setattr(self.smoothing_helper, name, value)
