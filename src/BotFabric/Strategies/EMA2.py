from src.BotFabric.Enums.StrategiesIDs import StrategiesIDs
from src.BotFabric.Interfaces.IStrategy import IStrategy


class EMA2(IStrategy):

    def __init__(self, fastPeriod=12, slowPeriod=26):
        self.name = StrategiesIDs.MA2
        self.fastPeriod = fastPeriod
        self.slowPeriod = slowPeriod

    def getName(self):
        return self.name

    def longestPeriod(self):
        return max(self.slowPeriod, 1)