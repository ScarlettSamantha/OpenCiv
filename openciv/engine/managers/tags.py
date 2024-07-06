from typing import Dict, List

# This object is a singleton
class _Tags():

    __instance: '_Tags' = None

    def __init__(self):
        self._tags: Dict[str, List[object]] = {}

    def add(self, tag: str, ref: object|List):
        if isinstance(ref, object):
            ref = [ref]
        for item in ref:
            self._tags[tag].append(ref)

    def tags(self, tag: str = None) -> Dict|List:
        return self._tags[tag] if tag is not None else self._tags

    @staticmethod
    def retrive_instance(cls) -> '_Tags':
        if cls.__instance is None:
            cls.__instance = _Tags()
        return cls.__instance

Tags = _Tags.retrive_instance()
