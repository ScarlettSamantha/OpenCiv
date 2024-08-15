from openciv.gameplay.great import GreatsTree
from openciv.engine.additions.pyload import PyLoad
from openciv.engine.managers.log import LogManager

from typing import Dict, NoReturn, Callable


class BaseCoreGreatsTree(GreatsTree):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.load_folder = None
        self._setup_saveable()

    def base_folder(self) -> str:
        return "openciv/gameplay/greats/"

    def load_greats_from_folder(self) -> NoReturn:
        folder = self.base_folder() + self.load_folder
        greats: Dict[str, Callable] = PyLoad.load_classes(folder)
        LogManager.get_instance().engine.debug(f"Loading Greats from {folder}")
        LogManager.get_instance().engine.debug(f"Greats found: {', '.join(greats.keys())}")
        for _, great in greats.items():
            self.add_great(great)
