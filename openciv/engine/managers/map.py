from __future__ import annotations
from openciv.engine.additions.hex_grid import HexGridRow, HexGrid
from openciv.engine.managers.base import BaseManager
from openciv.world.tiles._base_tile import BaseTile
import ast
from typing import Dict, Type
from openciv.engine.additions.pyload import PyLoad


class BaseTileVisitor(ast.NodeVisitor):
    def __init__(self):
        self.subclasses = []

    def visit_ClassDef(self, node: ast.ClassDef):
        for base in node.bases:
            if isinstance(base, ast.Name) and base.id == "BaseTile":
                self.subclasses.append(node.name)
        self.generic_visit(node)


class MapManager(BaseManager):
    def __init__(self, data: HexGrid = None):
        self._raw_data: HexGrid = data

        self._registered_tiles: Dict[str, Type[BaseTile]] = {}

    def load(self, tile_directory: str):
        # Will start to load the resources for the map.
        def load_tiles(directory: str) -> Dict[str, Type[BaseTile]]:
            classes = PyLoad.load_classes(directory, base_classes=BaseTile)
            return {key: classes[key] for key in classes if key not in ["BaseTile", "Tile"]}

        self._registered_tiles = load_tiles(tile_directory)

    def getDataRaw(self) -> HexGrid:
        return self._raw_data

    def setDataRaw(self, data: HexGrid):
        self._raw_data = data

    def __getitem__(self, row: int) -> HexGridRow:
        return self._raw_data[row]

    def __setitem__(self, row: int, data: HexGridRow):
        self._raw_data[row] = data

    def getTile(self, x: int, y: int) -> BaseTile:
        return self._raw_data[y][x]

    def setTile(self, x: int, y: int, tile: BaseTile):
        self._raw_data[y][x] = tile

    def getTileByPosition(self, x: int, y: int) -> BaseTile:
        for tile in self._registered_tiles.values():
            if tile.grid_position == (x, y):
                return tile

    def registeredTiles(self) -> Dict[str, Type[BaseTile]]:
        return self._registered_tiles

    def registerTile(self, tile: Type[BaseTile]):
        self._registered_tiles[tile.__name__] = tile
