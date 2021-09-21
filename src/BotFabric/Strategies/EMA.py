from typing import Union

from numpy import NaN

from src.BotFabric.Enums.Biases import Biases
from src.BotFabric.Enums.Orders import Orders
from src.BotFabric.Enums.StrategiesIDs import StrategiesIDs
from src.BotFabric.Interfaces.IStrategy import IStrategy
from src.BotFabric.StrategiesOrchestrator.WbeTechnicalAnalysis import WbeTechnicalAnalysis


class EMA(IStrategy):

    def __init__(self, period=200):
        super().__init__()
        self.name = StrategiesIDs.MA
        self.period = period
        self.lastEma = NaN
        self.ema = NaN

    def getName(self) -> StrategiesIDs:
        return self.name

    def setBiasStrategy(self, strategy: IStrategy):
        self.biasStrategy = strategy

    def longestPeriod(self):
        return max(self.period, 1)

    def update(self, dataset: list):
        self.orderSteer = Orders.NONE
        self.lastEma = self.ema
        self.ema = WbeTechnicalAnalysis.EMA(self.period, dataset)
        self.updateBiasSteer(dataset)
        self.updateOrderSteer(dataset)

    def updateBiasSteer(self, dataset: list):
        if dataset[0] > self.ema:
            self.biasSteer = Biases.BULL
        elif dataset[0] < self.ema:
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
