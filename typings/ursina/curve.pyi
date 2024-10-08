"""
This type stub file was generated by pyright.
"""

from ursina import *

"""
This type stub file was generated by pyright.
"""
def linear(t):
    ...

def in_sine(t):
    ...

def out_sine(t):
    ...

def in_out_sine(t):
    ...

def in_quad(t):
    ...

def out_quad(t):
    ...

def in_out_quad(t):
    ...

def in_cubic(t):
    ...

def out_cubic(t):
    ...

def in_out_cubic(t):
    ...

def in_quart(t):
    ...

def out_quart(t):
    ...

def in_out_quart(t):
    ...

def in_quint(t):
    ...

def out_quint(t):
    ...

def in_out_quint(t):
    ...

def in_expo(t):
    ...

def out_expo(t):
    ...

def in_out_expo(t):
    ...

def in_circ(t):
    ...

def out_circ(t):
    ...

def in_out_circ(t):
    ...

def in_back(t, magnitude=...):
    ...

def out_back(t, magnitude=...):
    ...

def in_out_back(t, magnitude=...):
    ...

def in_elastic(t, magnitude=...):
    ...

def out_elastic(t, magnitude=...):
    ...

def in_out_elastic(t, magnitude=...):
    ...

def out_bounce(t):
    ...

def in_bounce(t):
    ...

def in_out_bounce(t):
    ...

class CubicBezier:
    __slots__ = ...
    def __init__(self, a, b, c, d) -> None:
        ...

    def sample_curve_x(self, t):
        ...

    def sample_curve_y(self, t):
        ...

    def sample_curve_derivative_x(self, t):
        ...

    def calculate(self, x, epsilon=...):
        ...

    def solve_curve_x(self, t, epsilon=...):
        ...



if __name__ == '__main__':
    app = ...
    i = ...
    c = ...
