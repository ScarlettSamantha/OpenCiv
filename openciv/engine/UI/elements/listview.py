from __future__ import annotations
from ursina import Entity, color, mouse, Button
from typing import List


class ListView(Entity):
    def __init__(self, items: List[str], on_change: callable, title: str = "", **kwargs):
        super().__init__(**kwargs)
        self.items = items
        self.on_change = on_change
        self.title = title
        self.selected_index = 0
        self.is_open = False
        self.text_entities = []
        self.dropdown = None
        self.title_text = None

        self.selected_text = Button(
            text=f"{self.title}:     {self.items[self.selected_index]}",
            radius=-0.0,
            parent=self,
            scale=(10, 1),
            color=color.black,
            highlight_color=color.black,
        )

        # Create the dropdown list, initially hidden, with a black background
        self.dropdown = Entity(parent=self, enabled=False, position=(0, 0, -0.1))  # Move closer to the camera
        self.dropdown_background = Entity(
            parent=self.dropdown,
            model="quad",
            color=color.black,
            scale=(1.0, len(items) * 0.1 + 0.02),  # Adjusted scale to fit all items
            position=(
                0,
                -len(items) * 0.05 - 0.06,
                0.05,  # Move closer to the camera
            ),
        )
        self.highlight = Entity(
            parent=self.dropdown, model="quad", color=color.azure, scale=(5, 0.8), position=(0, 0, 0.04)
        )

        for i, item in enumerate(items):
            text_entity = Button(
                text=item if isinstance(item, object) else str(item),
                model="quad",
                radius=0.0,
                parent=self.dropdown,
                scale=(5, 0.8),
                position=(0, -i * 0.80 - 0.05, 0.05),  # Move closer to the camera
                color=color.black if i != self.selected_index else color.green,
                highlight_color=color.azure,
            )
            text_entity.on_click = self.create_click_handler(i)
            text_entity.on_mouse_enter = self.create_hover_handler(i)
            self.text_entities.append(text_entity)

        self.highlight.position = self.text_entities[self.selected_index].position

    def create_click_handler(self, index):
        def handler():
            self.select_item(index)

        return handler

    def create_hover_handler(self, index):
        def handler():
            self.highlight.position = self.text_entities[index].position
            self.selected_index = index

        return handler

    def calc_colors(self):
        for entity in self.text_entities:
            entity.color = color.black if self.selected_index != self.text_entities.index(entity) else color.green

    def toggle_dropdown(self):
        self.is_open = not self.is_open
        self.dropdown.enabled = self.is_open

    def input(self, key):
        if key == "left mouse down":
            if mouse.hovered_entity == self.selected_text:
                self.toggle_dropdown()

        if self.is_open:
            if key == "up arrow":
                self.selected_index = (self.selected_index - 1) % len(self.items)
                self.highlight.position = self.text_entities[self.selected_index].position
            elif key == "down arrow":
                self.selected_index = (self.selected_index + 1) % len(self.items)
                self.highlight.position = self.text_entities[self.selected_index].position
            elif key == "enter":
                self.select_item(self.selected_index)

    def select_item(self, index):
        self.selected_index = index
        self.selected_text.text = self.items[self.selected_index]
        self.calc_colors()
        self.toggle_dropdown()
        self.on_change(self.items[self.selected_index])

    @property
    def value(self):
        return self.items[self.selected_index]

    @value.setter
    def value(self, value):
        if value in self.items:
            self.selected_index = list(self.items.keys()).index(value)
            self.selected_text.text = value
            self.calc_colors()
        else:
            raise ValueError(f"Value {value} not in list of items")
