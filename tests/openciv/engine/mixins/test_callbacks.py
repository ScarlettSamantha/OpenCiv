from openciv.engine.mixins.callbacks import CallbacksMixin


class TestCallbacksMixin:
    def setup_method(self):
        self.manager = CallbacksMixin()

    def test_declare_event(self):
        self.manager._declare_event("new_event")
        assert "new_event" in self.manager._event_types()
        assert self.manager._events("new_event") == []

    def test_register_callback(self):
        self.manager._declare_event("event1")

        def dummy_callback(instance):
            pass

        self.manager.register_callback("event1", dummy_callback)
        assert dummy_callback in self.manager._events("event1")

    def test_unregister_callback(self):
        self.manager._declare_event("event2")

        def dummy_callback(instance):
            pass

        self.manager.register_callback("event2", dummy_callback)
        self.manager.unregister_callback("event2", dummy_callback)
        assert dummy_callback not in self.manager._events("event2")

    def test_trigger_callback(self):
        manager = CallbacksMixin()
        manager._declare_event("event3")

        def dummy_callback():
            assert True

        manager.register_callback("event3", dummy_callback)
        manager.trigger_callback("event3")

    def test_declare_events(self):
        manager = CallbacksMixin()
        events = ["event4", "event5"]
        manager._declare_events(events)
        for event in events:
            assert event in manager._event_types()
            assert manager._events(event) == []
