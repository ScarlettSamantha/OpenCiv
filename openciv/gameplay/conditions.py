from openciv.engine.saving import SaveAble


class Conditions(SaveAble):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._setup_saveable()
