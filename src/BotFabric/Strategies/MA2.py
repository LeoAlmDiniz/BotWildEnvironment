from src.Enums.Strategies import Strategies
from src.BotFabric.Interfaces.IStrategy import IStrategy


class MA2(IStrategy):

    def __init__(self, fastPeriod=50, slowPeriod=200):
        self.name = Strategies.MA2
        self.fastPeriod = fastPeriod
        self.slowPeriod = slowPeriod

    def getName(self):
        return self.name
