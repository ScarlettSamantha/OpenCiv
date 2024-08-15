from __future__ import annotations

from typing import Dict, List, Callable, Any, Optional, Union
from openciv.engine.managers.log import LogManager


class CallbacksMixin:
    ALL_CALLBACKS = -1

    def __init__(self):
        # Mapping event names to lists of dictionaries, each containing a callable and an optional dictionary of kwargs for the callable
        self.__callbacks: Dict[str, List[Dict[str, Union[Callable[..., Any], Optional[Dict[str, Any]]]]]] = {}

    def _event_types(self) -> List[str]:
        return list(self.__callbacks.keys())

    def _events(self, event: str) -> List[Callable[..., Any]] | Any:
        return [cb["callback"] for cb in self.__callbacks[event]]

    def _declare_event(self, event: str) -> None:
        LogManager.get_instance().engine.debug(msg=f"Declaring event: {event}")
        self.__callbacks[event] = []

    def _declare_events(self, events: List[str]) -> None:
        for event in events:
            self.__callbacks[event] = []

    def unregister_callback(self, event: str, callback: Callable[..., Any]) -> None:
        self.__callbacks[event] = [cb for cb in self.__callbacks[event] if cb["callback"] != callback]

    def trigger_all_callbacks(self, category: str, *args: Any, **kwargs: Any) -> None:
        self.trigger_callback(category=category, index=self.ALL_CALLBACKS, *args, **kwargs)

    def trigger_callback(self, category: str, index: int = ALL_CALLBACKS, *args: Any, **kwargs: Any) -> None:
        if len(self.__callbacks[category]) == 0:
            return

        def _trigger(
            item: Any | Callable[..., Any], item_kwargs: Any | Optional[Dict[str, Any]], *args: Any, **kwargs: Any
        ) -> None:
            LogManager.get_instance().engine.debug(f"Triggering callback: {item.__name__}")
            if item_kwargs is None:
                item_kwargs = {}
            item(self, *args, **item_kwargs, **kwargs)

        if index == self.ALL_CALLBACKS:
            for cb_dict in self.__callbacks[category]:
                _trigger(cb_dict["callback"], item_kwargs=cb_dict.get("kwargs"), *args, **kwargs)
        else:
            cb_dict = self.__callbacks[category][index]
            _trigger(cb_dict["callback"], item_kwargs=cb_dict.get("kwargs"), *args, **kwargs)

    def register_callback(self, event: str, callback: Callable[..., Any], **kwargs: Any) -> None:
        LogManager.get_instance().engine.debug(f"Registering callback: {callback.__name__} for event: {event}")
        self.__callbacks[event].append({"callback": callback, "kwargs": kwargs if kwargs else None})
