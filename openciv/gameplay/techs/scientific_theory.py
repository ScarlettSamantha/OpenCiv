from __future__ import annotations
from openciv.gameplay.tech import Tech
from openciv.engine.managers.i18n import _t


class ScientificTheory(Tech):
    def __init__(self, *args, **kwargs):
        super().__init__(
            "core.scientific_theory",
            _t("tech.scientific_theory.name"),
            _t("tech.scientific_theory.description"),
            tech_points_required=20,
            *args,
            **kwargs,
        )
