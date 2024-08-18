from __future__ import annotations
from openciv.gameplay.culture import Civic
from openciv.engine.managers.i18n import _t


class ClassAbolition(Civic):
    def __init__(self, *args, **kwargs):
        super().__init__(
            key="core.culture.civics.class_abolition",
            name=_t("content.culture.civics.core.class_abolition.name"),
            description=_t("content.culture.civics.core.class_abolition.description"),
            *args,
            **kwargs,
        )
