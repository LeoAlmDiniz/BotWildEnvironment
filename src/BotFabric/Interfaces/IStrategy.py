from abc import ABC, abstractproperty, abstractmethod
from typing import Union

from src.BotFabric.Enums.Biases import Biases
from src.BotFabric.Enums.Orders import Orders
from src.BotFabric.Enums.StrategiesIDs import StrategiesIDs


class IStrategy(ABC):

    def __init__(self):
        self.biasStrategy = None
        self.biasSteer = Biases.CRAB
        self.orderSteer = Orders.NONE

    @abstractmethod
    def getName(self) -> StrategiesIDs:
        raise NotImplementedError

    @abstractmethod
    def setBiasStrategy(self, strategy):
        raise NotImplementedError

    @abstractmethod
    def longestPeriod(self) -> int:
        raise NotImplementedError

    @abstractmethod
    def update(self, dataset: list):
        raise NotImplementedError


