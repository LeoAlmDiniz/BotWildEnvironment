from src.BotFabric.Interfaces.IExitTrigger import IExitTrigger
from src.BotFabric.Enums.ExitTriggersIDs import ExitTriggersIDs


class NoExit(IExitTrigger):

    def __init__(self):
        self.name = ExitTriggersIDs.NO_EXIT

    def getName(self):
        return self.name
