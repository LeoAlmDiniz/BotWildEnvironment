from src.BotFabric.Enums.StrategiesIDs import StrategiesIDs
from src.BotFabric.Interfaces.IStrategy import IStrategy


class MA2(IStrategy):

    def __init__(self, fastPeriod=12, slowPeriod=26):
        self.name = StrategiesIDs.MA2
        self.fastPeriod = fastPeriod
        self.slowPeriod = slowPeriod

    def getName(self) -> StrategiesIDs:
        return self.name

    def setBiasStrategy(self, strategy: IStrategy):
        self.biasStrategy = strategy

    def longestPeriod(self):
        return max(self.slowPeriod, 1)