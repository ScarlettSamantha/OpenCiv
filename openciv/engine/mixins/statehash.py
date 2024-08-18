from __future__ import annotations
import abc


class StateHashable(abc.ABC):
    @abc.abstractmethod
    def get_state_hash(self):
        pass
