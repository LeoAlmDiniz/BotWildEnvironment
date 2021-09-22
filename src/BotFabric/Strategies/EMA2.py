from typing import Union

from numpy import NaN

from src.BotFabric.Enums.Biases import Biases
from src.BotFabric.Enums.Orders import Orders
from src.BotFabric.Enums.StrategiesIDs import StrategiesIDs
from src.BotFabric.Interfaces.IStrategy import IStrategy
from src.BotFabric.Utils.WbeTechnicalAnalysis import WbeTechnicalAnalysis


class EMA2(IStrategy):

    def __init__(self, fastPeriod=12, slowPeriod=26, biasStrategy: Union[IStrategy, None] = None):
        super().__init__()
        self.name = StrategiesIDs.EMA2
        self.fastPeriod = fastPeriod
        self.slowPeriod = slowPeriod
        self.fastEma = NaN
        self.lastFastEma = NaN
        self.slowEma = NaN
        self.lastSlowEma = NaN

    def getName(self) -> StrategiesIDs:
        return self.name

    def setBiasStrategy(self, strategy: IStrategy):
        self.biasStrategy = strategy

    def longestPeriod(self):
        return max(self.slowPeriod, 1)

    def update(self, dataset: list):
        self.orderSteer = Orders.NONE
        self.lastFastEma = self.fastEma
        self.lastSlowEma = self.slowEma
        self.fastEma = WbeTechnicalAnalysis.EMA(self.fastPeriod, dataset)
        self.slowEma = WbeTechnicalAnalysis.EMA(self.slowPeriod, dataset)
        self.updateBiasSteer(dataset)
        self.updateOrderSteer(dataset)

    def updateBiasSteer(self, dataset: list):
        if self.fastEma > self.slowEma:
            self.biasSteer = Biases.BULL
        elif self.fastEma < self.slowEma:
            self.biasSteer = Biases.BEAR
        else:
            self.biasSteer = Biases.CRAB

    def updateOrderSteer(self, dataset: list):
        if self.biasStrategy.biasSteer == Biases.BULL and self.ema > dataset[0] >= self.lastEma:
            self.orderSteer = Orders.BUY
        elif self.biasStrategy.biasSteer == Biases.BEAR and self.ema < dataset[0] <= self.lastEma:
            self.orderSteer = Orders.SELL
        else:
            self.orderSteer = Orders.NONE