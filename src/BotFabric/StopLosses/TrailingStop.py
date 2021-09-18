from src.BotFabric.Enums.StopLossesIDs import StopLossesIDs
from src.BotFabric.Interfaces.IStopLoss import IStopLoss


class TrailingStop(IStopLoss):

    def __init__(self, gap):
        self.name = StopLossesIDs.TRAILINGSTOP
        self.gap = gap

    def getName(self):
        return self.name

    def getGap(self):
        return self.gap
