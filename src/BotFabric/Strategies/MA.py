from src.BotFabric.Enums.StrategiesIDs import StrategiesIDs
from src.BotFabric.Interfaces.IStrategy import IStrategy


class MA(IStrategy):

    def __init__(self, period=200):
        self.name = StrategiesIDs.MA
        self.period = period

    def getName(self):
        return self.name

    def longestPeriod(self):
        return max(self.period, 1)