class BaseManager:
    def __init__(self, parent: "BaseManager" = None):
        self.parent = parent

    def parent(self) -> "BaseManager":
        return self.parent

    def setParent(self, parent: "BaseManager") -> None:
        self.parent = parent
