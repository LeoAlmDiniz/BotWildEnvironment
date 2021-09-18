from src.BotFabric.Enums.StrategiesIDs import StrategiesIDs
from src.BotFabric.Interfaces.IStrategy import IStrategy


class RsiVwap(IStrategy):

    def __init__(self, period=14, anchor="D"):
        self.name = StrategiesIDs.RSIVWAP
        self.period = period
        self.anchor = anchor

    def getName(self):
        return self.name

    def longestPeriod(self):
        return max(self.period, 1)
