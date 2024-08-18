from __future__ import annotations
from typing import Any
from openciv.engine.mixins.callbacks import CallbacksMixin


class TestCallbacksMixin:
    def setup_method(self):
        self.manager = CallbacksMixin()

    def test_declare_event(self) -> None:
        self.manager._declare_event(event="new_event")  # type: ignore
        assert "new_event" in self.manager.event_types()
        assert self.manager.events(event="new_event") == []

    def test_register_callback(self) -> None:
        self.manager._declare_event(event="event1")  # type: ignore

        def dummy_callback(event: Any) -> None:
            pass

        self.manager.register_callback(event="event1", callback=dummy_callback)
        assert dummy_callback in self.manager.events(event="event1")

    def test_unregister_callback(self) -> None:
        self.manager._declare_event(event="event2")  # type: ignore

        def dummy_callback(instance: Any) -> None:
            pass

        self.manager.register_callback(event="event2", callback=dummy_callback)
        self.manager.unregister_callback(event="event2", callback=dummy_callback)
        assert dummy_callback not in self.manager.events("event2")

    def test_trigger_callback(self) -> None:
        manager = CallbacksMixin()
        manager._declare_event(event="event3")  # type: ignore

        def dummy_callback(event: Any) -> None:
            assert True

        manager.register_callback(event="event3", callback=dummy_callback)
        manager.trigger_callback(category="event3")

    def test_declare_events(self) -> None:
        manager = CallbacksMixin()
        events: list[str] = ["event4", "event5"]
        manager._declare_events(events=events)  # type: ignore
        for event in events:
            assert event in manager.event_types()
            assert manager.events(event=event) == []
