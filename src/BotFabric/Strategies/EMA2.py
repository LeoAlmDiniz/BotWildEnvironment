from typing import Union

from src.BotFabric.Enums.StrategiesIDs import StrategiesIDs
from src.BotFabric.Interfaces.IStrategy import IStrategy


class EMA2(IStrategy):

    def __init__(self, fastPeriod=12, slowPeriod=26, biasStrategy: Union[IStrategy, None] = None):
        super().__init__(biasStrategy)
        self.name = StrategiesIDs.MA2
        self.fastPeriod = fastPeriod
        self.slowPeriod = slowPeriod

    def getName(self) -> StrategiesIDs:
        return self.name

    def setBiasStrategy(self, strategy: IStrategy):
        self.biasStrategy = strategy

    def longestPeriod(self):
        return max(self.slowPeriod, 1)