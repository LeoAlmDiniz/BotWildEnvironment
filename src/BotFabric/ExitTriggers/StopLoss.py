from src.BotFabric.Interfaces.IExitTrigger import IExitTrigger
from src.Enums.ExitTriggers import ExitTriggers


class StopLoss(IExitTrigger):

    def __init__(self, gap):
        self.name = ExitTriggers.STOPLOSS

    def getName(self):
        return self.name