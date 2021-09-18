from src.BotFabric.Enums.StopLossesIDs import StopLossesIDs
from src.BotFabric.Interfaces.IStopLoss import IStopLoss


class NoStop(IStopLoss):

    def __init__(self, gap=0):
        self.name = StopLossesIDs.NO_STOP
        self.gap = gap

    def getName(self):
        return self.name

    def getGap(self):
        return self.gap
