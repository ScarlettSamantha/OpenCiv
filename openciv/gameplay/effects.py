from openciv.gameplay.effect import Effect


class Effects:
    def __init__(self, collection_name: str = None):
        from openciv.engine.managers.log import LogManager

        self.index = 0
        self.effects = {}
        self.collection_name: str | None = collection_name
        self.logger = LogManager._get_instance()

    def add(self, effect: Effect, auto_add_name_on_empty: bool = True):
        if auto_add_name_on_empty and getattr(effect, "name") is None:
            effect.name = f"!nameless_effect_from_{self.collection_name}_{self.index}"
        self.logger.loggers["gameplay"].debug(f"Adding effect {effect.name} to {self.collection_name}")
        self.effects[self.index] = effect
        self.index += 1

    def get(self, key):
        return self.effects[key]

    def delete(self, key):
        self.logger.logger("gameplay").debug(f"Deleting effect {self.effects[key].name} from {self.collection_name}")
        del self.effects[key]

    def toDict(self):
        return {index: effect.toDict() for index, effect in self.effects.items()}

    def __setitem__(self, key, effect: Effect):
        self.add(key, Effect)

    def __getitem__(self, _, key):
        return self.get(key)

    def __delitem__(self, key):
        self.delete(key)
