from typing import Dict, List, Callable


class CallbacksMixin:
    ALL_CALLBACKS = -1

    def __init__(self):
        self.__callbacks: Dict[str, List[callable]] = {}

    def _event_types(self) -> List[str]:
        return list(self.__callbacks.keys())

    def _events(self, event: str) -> List[Callable]:
        return self.__callbacks[event]

    def _declare_event(self, event: str):
        self.__callbacks[event] = []

    def _declare_events(self, events: List[str]):
        for event in events:
            self.__callbacks[event] = []

    def unregister_callback(self, event: str, callback: callable):
        self.__callbacks[event].remove(callback)

    def trigger_callback(self, category: str, index: int = ALL_CALLBACKS, *args, **kwargs):
        if (self.__callbacks[category]).__len__() > 0:
            return

        def _trigger(self, item: callable, *args, **kwargs):
            item(self, *args, **kwargs)

        if index == self.ALL_CALLBACKS:
            for item in self.__callbacks[category]:
                _trigger(self, item, *args, **kwargs)
        else:
            _trigger(self, self.__callbacks[category][index], *args, **kwargs)

    def register_callback(self, event: str, callback: callable):
        print(self.__callbacks)
        self.__callbacks[event].append(callback)
        print(self.__callbacks)
