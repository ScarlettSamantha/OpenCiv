from openciv.gameplay.city import City


class Cities:
    def __init__(self):
        self._cities = []

    def add(self, value: City):
        self._cities.append(value)

    def __iter__(self):
        self.index = 0

    def __len__(self) -> int:
        return len(self._cities)

    def __next__(self) -> City:
        if self.index >= self.__len__():
            raise StopIteration
        self.index += 1
        return self._cities[self.index]
