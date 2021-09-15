from src.Enums.StopLosses import StopLosses
from src.BotFabric.Interfaces.IStopLoss import IStopLoss


class NoStop(IStopLoss):

    def __init__(self, gap=0):
        self.name = StopLosses.NO_STOP
        self.gap = gap

    def getName(self):
        return self.name

    def getGap(self):
        return self.gap
