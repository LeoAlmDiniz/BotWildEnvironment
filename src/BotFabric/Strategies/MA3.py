from src.BotFabric.Enums.StrategiesIDs import StrategiesIDs
from src.BotFabric.Interfaces.IStrategy import IStrategy


class MA3(IStrategy):

    def __init__(self, fastPeriod=13, neutralPeriod=21, slowPeriod=34):
        self.name = StrategiesIDs.MA3
        self.fastPeriod = fastPeriod
        self.neutralPeriod = neutralPeriod
        self.slowPeriod = slowPeriod

    def getName(self) -> StrategiesIDs:
        return self.name

    def setBiasStrategy(self, strategy: IStrategy):
        self.biasStrategy = strategy

    def longestPeriod(self):
        return max(self.slowPeriod, 1)