from __future__ import annotations
from typing import Dict, List
from openciv.engine.mixins.singleton import Singleton


class Tag:
    def __init__(self, tag: str, instance: object):
        self._tag: str = tag
        self._tag_instance: object = instance

    def tag(self) -> str:
        return self._tag

    def instance(self) -> object:
        return self._tag_instance

    def __repr__(self) -> str:
        return self._tag


class _Tags(Singleton):
    def __setup__(self):
        self._tags: Dict[str, List[object]] = {}

    def add(self, tag: Tag):
        if tag.tag() not in self._tags:
            self._tags[tag.tag()] = []
        self._tags[tag.tag()].append(tag.instance())

    def tags(self, tag: str = None) -> Dict | List:
        return self._tags[tag] if tag is not None else self._tags


class Taggable:
    def __init__(self):
        self.tags: List[Tag] = []

    def add_tag(self, tag: Tag):
        self.tags.append(tag)
        _Tags.get_instance().add(tag)

    def has_tag(self, tag: str) -> bool:
        return any(t.tag == tag for t in self.tags)

    def remove_tag(self, tag: str):
        self.tags = [t for t in self.tags if t.tag() != tag]

    def get_tag(self, tag: str) -> Tag:
        return next(t for t in self.tags if t.tag() == tag)

    def get_tags(self) -> List[Tag]:
        return self.tags

    def get_tag_instances(self, tag: str) -> List[object]:
        return [t.instance for t in self.tags if t.tag() == tag()]

    def get_all_tags(self) -> List[str]:
        return [t.tag for t in self.tags]

    def get_all_tag_instances(self) -> List[object]:
        return [t.instance for t in self.tags]

    def clear_tags(self):
        self.tags = []
