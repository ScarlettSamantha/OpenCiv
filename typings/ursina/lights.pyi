"""
This type stub file was generated by pyright.
"""

from ursina import Entity

"""
This type stub file was generated by pyright.
"""
class Light(Entity):
    def __init__(self, **kwargs) -> None:
        ...

    @property
    def color(self):
        ...

    @color.setter
    def color(self, value):
        ...



class DirectionalLight(Light):
    def __init__(self, shadows=..., **kwargs) -> None:
        ...

    @property
    def shadows(self):
        ...

    @shadows.setter
    def shadows(self, value):
        ...

    def update_bounds(self, entity=...):
        ...



class PointLight(Light):
    def __init__(self, **kwargs) -> None:
        ...



class AmbientLight(Light):
    def __init__(self, **kwargs) -> None:
        ...



class SpotLight(Light):
    def __init__(self, **kwargs) -> None:
        ...



if __name__ == '__main__':
    app = ...
    light = ...
    dont_cast_shadow = ...
    unlit_entity = ...
    bar = ...
