from openciv.engine.UI.menu import Menu
from ursina import camera, color, window
from openciv.engine.entity import Entity

from abc import ABC


class TestMenu(Menu, ABC):
    def __init__(self, game_manager, call: callable, *args, **kwargs):
        pass
