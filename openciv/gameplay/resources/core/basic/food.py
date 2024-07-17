from openciv.gameplay.resources.core.basic._base import BasicBaseResource
from openciv.engine.managers.i18n import _t


class Food(BasicBaseResource):
    def __init__(self, value, *args, **kwargs):
        super().__init__(
            "core.basic.food",
            _t("content.resources.food.name"),
            _t("content.resources.food.description"),
            value,
            *args,
            **kwargs,
        )
