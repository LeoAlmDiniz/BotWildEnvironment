from src.BotFabric.Interfaces.IExitTrigger import IExitTrigger
from src.BotFabric.Enums.ExitTriggersIDs import ExitTriggersIDs


class StopLoss(IExitTrigger):

    def __init__(self, gap):
        self.name = ExitTriggersIDs.STOPLOSS

    def getName(self):
        return self.name