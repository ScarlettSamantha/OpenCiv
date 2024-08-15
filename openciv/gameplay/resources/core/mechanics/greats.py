from openciv.gameplay.resources.core.mechanics._base import BaseGreatMechanicResource
from openciv.engine.managers.i18n import _t
from typing import Union


class GreatScientist(BaseGreatMechanicResource):
    def __init__(self, value: Union[float | int], *args, **kwargs):
        super().__init__(
            "core.mechanic.great_person_science",
            _t("content.resources.great_person_science.name"),
            _t("content.resources.great_person_science.description"),
            value,
            *args,
            **kwargs,
        )


class GreatArtist(BaseGreatMechanicResource):
    def __init__(self, value: Union[float | int], *args, **kwargs):
        super().__init__(
            "core.mechanic.great_person_culture",
            _t("content.resources.great_person_culture.name"),
            _t("content.resources.great_person_culture.description"),
            value,
            *args,
            **kwargs,
        )


class GreatHero(BaseGreatMechanicResource):
    def __init__(self, value: Union[float | int], *args, **kwargs):
        super().__init__(
            "core.mechanic.great_person_hero",
            _t("content.resources.great_person_hero.name"),
            _t("content.resources.great_person_hero.description"),
            value,
            *args,
            **kwargs,
        )


class GreatHoly(BaseGreatMechanicResource):
    def __init__(self, value: Union[float | int], *args, **kwargs):
        super().__init__(
            "core.mechanic.great_person_faith",
            _t("content.resources.great_person_faith.name"),
            _t("content.resources.great_person_faith.description"),
            value,
            *args,
            **kwargs,
        )


class GreatMilitary(BaseGreatMechanicResource):
    def __init__(self, value: Union[float | int], *args, **kwargs):
        super().__init__(
            "core.mechanic.great_person_military",
            _t("content.resources.great_person_military.name"),
            _t("content.resources.great_person_military.description"),
            value,
            *args,
            **kwargs,
        )


class GreatEngineer(BaseGreatMechanicResource):
    def __init__(self, value: Union[float | int], *args, **kwargs):
        super().__init__(
            "core.mechanic.great_person_engineer",
            _t("content.resources.great_person_engineer.name"),
            _t("content.resources.great_person_engineer.description"),
            value,
            *args,
            **kwargs,
        )


class GreatCommerece(BaseGreatMechanicResource):
    def __init__(self, value: Union[float | int], *args, **kwargs):
        super().__init__(
            "core.mechanic.great_person_commerece",
            _t("content.resources.great_person_commerece.name"),
            _t("content.resources.great_person_commerece.description"),
            value,
            *args,
            **kwargs,
        )


class GreatExplorer(BaseGreatMechanicResource):
    def __init__(self, value: Union[float | int], *args, **kwargs):
        super().__init__(
            "core.mechanic.great_person_explorer",
            _t("content.resources.great_person_explorer.name"),
            _t("content.resources.great_person_explorer.description"),
            value,
            *args,
            **kwargs,
        )
