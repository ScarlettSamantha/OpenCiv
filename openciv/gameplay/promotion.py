from __future__ import annotations

from openciv.engine.managers.i18n import T_TranslationOrStr
from openciv.engine.saving import SaveAble
from openciv.gameplay.effect import Effects
from openciv.gameplay.combat.stats import Stats
from openciv.engine.requires import Requires, RequiresMultiple, T_Requires
from openciv.engine.mixins.callbacks import CallbacksMixin

from typing import List, Any, Iterable, Self
from abc import abstractmethod


class Promotion(SaveAble, CallbacksMixin):
    def __init__(
        self,
        key: str,
        name: T_TranslationOrStr,
        description: T_TranslationOrStr,
        icon: str,
        aquired: bool = False,
        requires: T_Requires = None,
        combat_stats: Stats = Stats(),
        *args: Any,
        **kwargs: Any,
    ):
        SaveAble.__init__(self, *args, **kwargs)
        CallbacksMixin.__init__(self, *args, **kwargs)
        self.key: str = key
        self.name: T_TranslationOrStr = name
        self.description: T_TranslationOrStr = description
        self.icon: str = icon
        self._requires: T_Requires = requires
        self.effects: Effects = Effects()
        self.combat_stats: Stats = combat_stats

        self.aquired: bool = aquired
        self._setup_saveable()

    @property
    def requires(self) -> T_Requires:
        return self._requires

    @requires.setter
    def requires(self, requires: T_Requires) -> Self:
        if isinstance(requires, Iterable) and not isinstance(requires, (str, bytes)):
            # Convert Iterable to a list
            self._requires = RequiresMultiple.convert_from_list(conditions=requires)
        else:
            self._requires = requires
        return self

    def declare_events(self) -> None:
        self._declare_event(event="on_aquire")
        self._declare_event(event="on_unaquire")

    def are_requirements_met(self) -> bool:
        if self.requires is None:
            return True
        if isinstance(self.requires, (Requires, RequiresMultiple)):
            return self.requires.checkCondition()
        if isinstance(self.requires, list):
            return all(req.checkCondition() for req in self.requires)
        return False

    def aquire(self) -> Promotion:
        self.aquired = True
        self.trigger_callback(category="on_aquire", promotion=self)
        return self

    def unaquire(self) -> Promotion:
        self.aquired = False
        self.trigger_callback(category="on_unaquire", promotion=self)
        return self

    def is_locked(self) -> bool:
        if self.requires is None:
            return False
        if isinstance(self.requires, (Requires, RequiresMultiple)):
            return self.requires.checkCondition()
        if isinstance(self.requires, list):
            return all(req.checkCondition() for req in self.requires)
        return False


class PromotionTree(SaveAble, CallbacksMixin):
    def __init__(
        self,
        key: str,
        name: T_TranslationOrStr,
        description: T_TranslationOrStr,
        icon: str,
        unlocked: bool = False,
        unlock_requires: T_Requires = None,
        *args: Any,
        **kwargs: Any,
    ):
        SaveAble().__init__(*args, **kwargs)
        CallbacksMixin().__init__(*args, **kwargs)
        self.key: str = key
        self.name: T_TranslationOrStr = name
        self.description: T_TranslationOrStr = description
        self.promotions: List[Promotion] = []
        self.icon: str = icon
        self.requires: T_Requires = unlock_requires
        self.unlocked: bool = unlocked

        # Unlike the Promotion class, we don't have a combat_stats attribute here as we need to calculate the effects of all promotions in the tree.
        self.combat_stats: Stats = Stats()
        self.completion_effects: Effects = Effects()
        self.begin_effects: Effects = Effects()
        self._effects: Effects | None = None
        self.register_promotions()
        self._setup_saveable()

    @abstractmethod
    def register_promotions(self) -> None:
        pass

    def _on_promotion_aquire(
        self, promotion: Promotion, sub_trigger_aquire: bool = True, sub_trigger_completion_check: bool = True
    ) -> None:
        self.calculate_effects()
        if sub_trigger_aquire:
            self.trigger_callback(category="on_promotion_aquire", promotion=promotion, promotion_tree=self)
        if sub_trigger_completion_check and self.completed():
            self.trigger_callback(category="on_complete", promotion_tree=self)

    def _on_promotion_unaquire(
        self, promotion: Promotion, sub_trigger_unaquire: bool = True, sub_trigger_completion_check: bool = True
    ) -> None:
        self.calculate_effects()
        if sub_trigger_unaquire:
            self.trigger_callback(category="on_promotion_unaquire", promotion=promotion, promotion_tree=self)
        if sub_trigger_completion_check and not self.completed():
            self.trigger_callback(category="on_unaquire", promotion_tree=self)

    def add_promotion(self, promotion: Promotion) -> PromotionTree:
        promotion.register_callback(event="on_aquire", callback=self._on_promotion_aquire)
        self.promotions.append(promotion)
        return self

    def remove_promotion(self, promotion: Promotion) -> PromotionTree:
        promotion.unregister_callback(event="on_un_aquire", callback=self._on_promotion_unaquire)
        self.promotions.remove(promotion)
        return self

    def declare_events(self) -> None:
        self._declare_event(event="on_unlock")
        self._declare_event(event="on_lock")
        self._declare_event(event="on_complete")
        self._declare_event(event="on_promotion_aquire")
        self._declare_event(event="on_promotion_unaquire")

    def calculate_effects(self, force: bool = False) -> Effects:
        if force is False or self._effects is None:
            self._effects = Effects()
            for promotion in self.promotions:
                if promotion.aquired:
                    self._effects += promotion.effects
        return self._effects

    def is_locked(self) -> bool:
        if self.requires is None:
            return False
        if isinstance(self.requires, (Requires, RequiresMultiple)):
            return self.requires.checkCondition()
        if isinstance(self.requires, list):
            return all(req.checkCondition() for req in self.requires)
        return False

    def unlock(self) -> PromotionTree:
        self.unlocked = True
        self.trigger_callback(category="on_unlock", promotion_tree=self)
        return self

    def lock(self) -> PromotionTree:
        self.unlocked = False
        self.trigger_callback(category="on_lock", promotion_tree=self)
        return self

    @property
    def effects(self) -> Effects:
        if self._effects is None:
            self.calculate_effects()
        effects = Effects()
        for promotion in self.promotions:
            if promotion.aquired:
                effects += promotion.effects
        return effects

    @effects.setter
    def effects(self, effects: Effects) -> None:
        self._effects = effects

    def completed(self) -> bool:
        return all([promotion.aquired for promotion in self.promotions])

    def stats(self) -> dict[str, bool | int]:
        return {
            "unlocked": self.unlocked,
            "num_promotions": len(self.promotions),
            "num_aquired": len([promotion for promotion in self.promotions if promotion.aquired]),
        }
