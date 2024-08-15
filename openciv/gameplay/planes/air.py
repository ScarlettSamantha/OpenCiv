from __future__ import annotations

from openciv.gameplay.planes.plane import Plane
from openciv.engine.managers.i18n import t_
from typing import Any


class Air(Plane):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(
            key="core.plane.air",
            name=t_("content.planes.core.air.name"),
            description=t_("content.planes.core.air.description"),
            *args,
            **kwargs,
        )
