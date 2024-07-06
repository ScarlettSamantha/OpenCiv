from openciv.engine.exceptions.manager_exception import ManagerException


class TechException(ManagerException):
    def __init__(self, *args, **kwargs):
        ManagerException.__init__(self, *args, **kwargs)


class TechNotFoundException(TechException):
    def __init__(self, *args, **kwargs):
        TechException.__init__(self, *args, **kwargs)
