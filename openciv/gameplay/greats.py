class Greats:
    # This block is for IDE syntax sugar.
    scientist = "scientist"
    engineer = "engineer"
    general = "general"
    admiral = "admiral"
    commerce = "commerce"
    fatih = "faith"
    creative = "creative"
    hero = "hero"

    def __init__(self):
        self.scientist = 0
        self.engineer = 0
        self.general = 0
        self.admiral = 0
        self.commerce = 0
        self.faith = 0
        self.creative = 0
        self.hero = 0

    def addPoint(self, property, amount: int):
        setattr(self, property, getattr(self, property) + amount)

    def decreasePoints(self, property, amount: int):
        setattr(self, property, getattr(self, property) - amount)

    def setPoints(self, property, amount: int):
        setattr(self, property, amount)
