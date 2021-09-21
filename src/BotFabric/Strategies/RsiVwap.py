from src.BotFabric.Enums.StrategiesIDs import StrategiesIDs
from src.BotFabric.Interfaces.IStrategy import IStrategy


class RsiVwap(IStrategy):

    def __init__(self, period=14, anchor="D"):
        self.name = StrategiesIDs.RSIVWAP
        self.period = period
        self.anchor = anchor

    def getName(self) -> StrategiesIDs:
        return self.name

    def setBiasStrategy(self, strategy: IStrategy):
        self.biasStrategy = strategy

    def longestPeriod(self):
        return max(self.period, 1)
