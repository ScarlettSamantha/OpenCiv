from __future__ import annotations
from openciv.gameplay.great import Great
from openciv.gameplay.resources.core.basic.gold import Gold


class CoreGreat(Great):
    def __init__(self, *args, **kwargs):
        super().__init__(resource_type_required=Gold, *args, **kwargs)
