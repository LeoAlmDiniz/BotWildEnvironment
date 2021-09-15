from src.Enums.StopLosses import StopLosses
from src.BotFabric.Interfaces.IStopLoss import IStopLoss


class TrailingStop(IStopLoss):

    def __init__(self, gap):
        self.name = StopLosses.TRAILINGSTOP
        self.gap = gap

    def getName(self):
        return self.name

    def getGap(self):
        return self.gap
