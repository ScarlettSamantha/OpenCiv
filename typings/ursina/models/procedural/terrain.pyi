"""
This type stub file was generated by pyright.
"""

from ursina import *

"""
This type stub file was generated by pyright.
"""
def texture_to_height_values(heightmap, skip=...):
    ...

class Terrain(Mesh):
    def __init__(self, heightmap=..., height_values=..., gradient=..., skip=..., **kwargs) -> None:
        ...

    def generate(self):
        ...



if __name__ == '__main__':
    app = ...
    terrain_from_heightmap_texture = ...
    hv = ...
    terrain_from_list = ...
    terrain_bounds = ...
    def input(key):
        ...

    player = ...
    def update():
        ...

