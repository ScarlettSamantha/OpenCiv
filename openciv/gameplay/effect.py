class Effect:
    TILE = 0
    CITY = 1
    PROVINCE = 2
    PLAYER = 3
    GLOBAL = 4
    RADIUS = 5
    FIXED = 6
    # This is to bypass the need to have a target. It will always target the player that is currently active.
    # This is due to a circuler import issue and objects then being very linked which is kinda slow.
    PLAYER_CURRENT = 7

    def __init__(self, name: str = "", target=None, domain: int = TILE):
        self.active: bool = True
        self.name = name

        self.target = target
        self.domain = None

        self._mechanics = []

        self._links = []
        self._tags = []

        self._conditions = []
