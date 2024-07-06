from openciv.engine.managers.base import BaseManager
from collections import OrderedDict
from openciv.gameplay.tech import Tech
from typing import List
from openciv.engine.mixins.callbacks import CallbacksMixin
from openciv.engine.additions.pyload import PyLoad


class TechManager(BaseManager, CallbacksMixin, PyLoad):
    def __init__(self, game, technology_folders: List = []):
        BaseManager.__init__(self, game)
        CallbacksMixin.__init__(self)
        PyLoad.__init__(self)

        self.queue: OrderedDict[int, Tech] = OrderedDict()
        self.registered_techs: List[Tech] = []

        self._needed_science: int = 1
        self._current_science_pool: int = 0
        self._tech_tree = None

        self.declare_events()
        self.process_folders(technology_folders)

    @property
    def needed_science(self) -> int:
        return self._needed_science

    @needed_science.setter
    def needed_science(self, value: int):
        self._needed_science = value

    @property
    def current_science(self) -> int:
        return self._current_science_pool

    @current_science.setter
    def current_science(self, value: int):
        self._current_science_pool = value

    def log(self):
        parent: "GameManager" = self.parent()  # noqa F821
        return parent.log()

    def declare_events(self):
        self._declare_event("on_tech_researched")
        self._declare_event("on_tech_queue_updated")
        self._declare_event("on_tech_added")
        self._declare_event("on_tech_reorder")
        self._declare_event("on_science_added")
        self._declare_event("on_science_removed")

    def process_folders(self, folders: List):
        def process_folder(folder):
            classes = PyLoad.load_classes(folder)
            for _class in classes:
                if not isinstance(_class, Tech):
                    self.log().gameplay.warning(f"Class is not a tech: {_class}")
                    continue
                self.log().gameplay.debug(f"Adding tech: {_class}")
                self.add_tech(_class)

        for folder in folders:
            process_folder(folder)

    def add_tech_to_queue(self, tech: Tech) -> None:
        self.queue[len(self.queue)] = tech
        self.trigger_callback("on_tech_queue_updated")

    def reorder(self) -> None:
        self.queue = OrderedDict((i, tech) for i, tech in enumerate(self.queue.values()))
        self.trigger_callback("on_tech_reorder")

    def do_first_queue(self, tech: Tech) -> None:
        self.queue = OrderedDict([(0, tech)] + [(i + 1, t) for i, t in enumerate(self.queue.values())])
        self.trigger_callback("on_tech_queue_updated")

    def delete_tech(self, tech: Tech) -> None:
        self.registered_techs.remove(tech)

    def add_tech(self, tech: Tech) -> None:
        self.registered_techs.append(tech)
        self.trigger_callback("on_tech_added")

    def current_tech(self) -> Tech | None:
        return self.queue[0] if self.queue else None

    def next_tech(self) -> Tech | None:
        return self.queue[1] if len(self.queue) > 1 else None

    def process_queue(self) -> None:
        if self.queue:
            self.queue.pop(0)
            self.reorder()
            self.trigger_callback("on_tech_queue_updated")

    def complete_research(self, auto_complete_tech: bool = True) -> None:
        self._current_science_pool -= self._needed_science
        self.process_queue()
        self.trigger_callback("on_tech_researched")

        # We check if we can still complete more for example if the player gets a large amount of science it could complete 1 or more techs.
        if auto_complete_tech and self._current_science_pool >= self._needed_science:
            self.complete_research()

    def add_science(self, science: int, auto_complete_tech: bool = True) -> None:
        self._current_science_pool += science
        self.trigger_callback("on_science_added")

        while auto_complete_tech and self._current_science_pool >= self._needed_science and self.queue:
            self.complete_research(auto_complete_tech=auto_complete_tech)

    def remove_science(self, science: int):
        self._current_science_pool -= science
        if self._current_science_pool < 0:
            self._current_science_pool = 0
        self.trigger_callback("on_science_removed")
