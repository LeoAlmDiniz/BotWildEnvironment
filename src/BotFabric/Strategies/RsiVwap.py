from src.Enums.Strategies import Strategies
from src.BotFabric.Interfaces.IStrategy import IStrategy
from src.Enums.Timeframes import Timeframes


class RsiVwap(IStrategy):

    def __init__(self, period=14, anchor="D"):
        self.name = Strategies.RSIVWAP
        self.period = period
        self.anchor = anchor

    def getName(self):
        return self.name
