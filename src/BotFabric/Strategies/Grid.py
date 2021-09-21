from typing import Union

import numpy as np
from numpy import NaN

from src.BotFabric.Enums.Biases import Biases
from src.BotFabric.Enums.Orders import Orders
from src.BotFabric.Enums.StrategiesIDs import StrategiesIDs
from src.BotFabric.Interfaces.IStrategy import IStrategy


class Grid(IStrategy):

    def __init__(self, angle=0, gridDefaultSpacing=0.03):
        super().__init__()
        self.name = StrategiesIDs.GRID
        self.biasModifier = float(np.invert(np.cos(np.deg2rad(angle))))
        self.priceLevel = NaN
        self.gridDefaultSpacing = gridDefaultSpacing

    def getName(self) -> StrategiesIDs:
        return self.name

    def setBiasStrategy(self, strategy: IStrategy):
        self.biasStrategy = strategy

    def longestPeriod(self):
        return 1

    def update(self, dataset: list):
        if dataset[0] <= self.priceLevel * (1 - self.gridDefaultSpacing):
            self.orderSteer = Orders.BUY
            self.priceLevel = dataset[0]
        elif dataset[0] >= self.priceLevel * (1 + self.gridDefaultSpacing):
            self.orderSteer = Orders.SELL
            self.priceLevel = dataset[0]
