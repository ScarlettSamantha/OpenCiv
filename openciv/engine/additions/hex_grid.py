from ursina import Vec3, Entity
from openciv.world.tiles._base_tile import BaseTile, Tile
from openciv.engine.exceptions.argument_exception import ArgumentException
from typing import Dict, List
import random
import math


class HexGridRow:
    def __init__(self):
        self._data = {}

    def add(self, key, item):
        self._data[key] = item

    def get(self, key):
        return self._data[key]

    def __getitem__(self, _, b):
        return self.get(b)


class HexGrid(Entity):
    def __init__(self, width: int, height: int, radius: float = 1.0, tiles: List = [], **kwargs):
        if tiles == []:
            raise ArgumentException("Tiles must be provided to HexGrid")

        super().__init__(**kwargs)
        self.width = width
        self.height = height
        self.radius = radius

        hex_width = math.sqrt(3) * radius
        hex_height = 2 * radius
        vert_offset = hex_height * 3 / 4

        self.grid: Dict(int, Dict(int, BaseTile)) = {}

        for y in range(height):
            row = HexGridRow()
            for x in range(width):
                center_x = x * hex_width
                center_y = y * vert_offset
                if y % 2 == 1:
                    center_x += hex_width / 2

                position = Vec3(center_x, 0, center_y)

                row.add(x, Tile(tile=random.choice(list(tiles.values())), position=position, x=x, y=y))
            self.grid[y] = row
