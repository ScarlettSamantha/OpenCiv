from __future__ import annotations
from openciv.gameplay.culture import CultureSubtree


class BaseCoreSubtree(CultureSubtree):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
