from openciv.gameplay.city import City
from typing import List, Iterator


class Cities:
    def __init__(self) -> None:
        self._cities: List[City] = []

    def add(self, value: City) -> None:
        self._cities.append(value)

    def __iter__(self) -> Iterator[City]:
        self.index = 0
        return self

    def __len__(self) -> int:
        return len(self._cities)

    def __next__(self) -> City:
        if self.index >= len(self._cities):
            raise StopIteration
        city: City = self._cities[self.index]
        self.index += 1
        return city
