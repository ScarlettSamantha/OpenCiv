"""
This type stub file was generated by pyright.
"""

"""
This type stub file was generated by pyright.
"""
class Texture:
    default_filtering = ...
    def __init__(self, value, filtering=...) -> None:
        ...

    @staticmethod
    def new(size, color=...):
        ...

    @property
    def name(self):
        ...

    def __str__(self) -> str:
        ...

    @property
    def size(self):
        ...

    @property
    def width(self):
        ...

    @property
    def height(self):
        ...

    @property
    def pixels(self):
        ...

    @property
    def filtering(self):
        ...

    @filtering.setter
    def filtering(self, value):
        ...

    @property
    def repeat(self):
        ...

    @repeat.setter
    def repeat(self, value):
        ...

    def get_pixel(self, x, y):
        ...

    def get_pixels(self, start, end):
        ...

    def set_pixel(self, x, y, color):
        ...

    def apply(self):
        ...

    def save(self, path):
        ...

    def __repr__(self):
        ...

    def __del__(self):
        ...



if __name__ == '__main__':
    app = ...
    e = ...
    e = ...
    def input(key):
        ...

    tex = ...
