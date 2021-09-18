from src.BotFabric.Interfaces.IExitTrigger import IExitTrigger
from src.BotFabric.Enums.ExitTriggersIDs import ExitTriggersIDs


class RealiseProfit(IExitTrigger):

    def __init__(self, gap):
        self.name = ExitTriggersIDs.REALISE_PROFIT

    def getName(self):
        return self.name