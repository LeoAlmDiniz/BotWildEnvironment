from src.BotFabric.Interfaces.IExitTrigger import IExitTrigger
from src.Enums.ExitTriggers import ExitTriggers


class RealiseProfit(IExitTrigger):

    def __init__(self, gap):
        self.name = ExitTriggers.REALISE_PROFIT

    def getName(self):
        return self.name