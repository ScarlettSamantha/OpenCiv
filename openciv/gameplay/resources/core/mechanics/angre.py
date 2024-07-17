from openciv.gameplay.resources.core.mechanics._base import MechanicBaseResource
from openciv.engine.managers.i18n import _t
from typing import Union


class Angre(MechanicBaseResource):
    def __init__(self, value: Union[float | int], *args, **kwargs):
        super().__init__(
            "core.mechanic.angre",
            _t("content.resources.angre.name"),
            _t("content.resources.angre.description"),
            value,
            *args,
            **kwargs,
        )
