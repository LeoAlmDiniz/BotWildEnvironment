from src.Enums.Strategies import Strategies
from src.BotFabric.Interfaces.IStrategy import IStrategy
from src.Enums.Timeframes import Timeframes


class MA3(IStrategy):

    def __init__(self, fastPeriod=13, neutralPeriod=21, slowPeriod=34):
        self.name = Strategies.MA3
        self.fastPeriod = fastPeriod
        self.neutralPeriod = neutralPeriod
        self.slowPeriod = slowPeriod

    def getName(self):
        return self.name

