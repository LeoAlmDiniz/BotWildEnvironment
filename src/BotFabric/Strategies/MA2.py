from src.BotFabric.Enums.StrategiesIDs import StrategiesIDs
from src.BotFabric.Interfaces.IStrategy import IStrategy


class MA2(IStrategy):

    def __init__(self, fastPeriod=50, slowPeriod=200):
        self.name = StrategiesIDs.MA2
        self.fastPeriod = fastPeriod
        self.slowPeriod = slowPeriod

    def getName(self):
        return self.name

    def longestPeriod(self):
        return max(self.slowPeriod, 1)