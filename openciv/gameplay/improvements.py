from __future__ import annotations
from typing import List


class Improvements:
    def __init__(self, improvements: List = None):
        self._improvements = {}
        if improvements is not None:
            for item in improvements:
                self.add(item)

    def add(self, value: "improvement"):  # noqa F821
        self._improvements[len(self._improvements.keys())] = value

    def __add__(self, value: "improvement"):  # noqa F821
        self.add(value)
        return self
