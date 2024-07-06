from openciv.gameplay.effects import Effects


class Leader:
    def __init__(self):
        self.name = None
        self.icon = None
        self.description = None

        self._effects = Effects()

    def add_effect(self, effect):
        self._effects.add(effect)

    def get_effects(self):
        return self._effects
