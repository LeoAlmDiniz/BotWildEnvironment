from src.BotFabric.Interfaces.IExitTrigger import IExitTrigger
from src.Enums.ExitTriggers import ExitTriggers


class NoExit(IExitTrigger):

    def __init__(self):
        self.name = ExitTriggers.NO_EXIT

    def getName(self):
        return self.name
