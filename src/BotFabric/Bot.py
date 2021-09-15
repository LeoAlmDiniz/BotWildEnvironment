
from src.Enums.ExitTriggers import ExitTriggers
from src.Enums.StopLosses import StopLosses
from src.Enums.Strategies import Strategies
from src.Enums.Timeframes import Timeframes
from src.BotFabric.Errors.IncompatibleBotError import IncompatibleBotException
from src.BotFabric.Interfaces.IBot import IBot
from src.BotFabric.Interfaces.IStopLoss import IStopLoss
from src.BotFabric.Interfaces.IStrategy import IStrategy
from src.BotFabric.Interfaces.IExitTrigger import IExitTrigger

import uuid


class Bot(IBot):

    def __init__(self, strategy: IStrategy,
                 timeframe: Timeframes,
                 biased: bool,
                 biasStrategy: IStrategy,
                 stopLossType: IStopLoss,
                 exitTrigger: IExitTrigger,
                 maxPyramiding: int):
        self.id = uuid.uuid4()
        self.strategy = strategy  # Injetar object IStrategy
        self.timeframe = timeframe  # Enum Timeframes
        self.biased = biased  # true => o bot opera alterando apenas longs ou apenas shorts; false => o bot operando
        # long e short ao mesmo tempo;
        if self.biased:
            self.biasStrategy = biasStrategy  # Injetar object IStrategy
        else:
            self.biasStrategy = None
        self.stopLossType = stopLossType  # Injetar object IStopLoss
        self.exitTrigger = exitTrigger  # Enum ExitTriggers
        self.maxPyramiding = maxPyramiding  # 0 = wont ever pyramid
        self.score = 0
        self.unrealisedBalance = 0
        self.maxUnrealisedLoss = 0
        self.maxDrawdown = 0
        self.applyRestrictions()

    def applyRestrictions(self):
        if self.strategy.getName() == Strategies.GRID and self.exitTrigger.getName() != ExitTriggers.NO_EXIT:
            raise IncompatibleBotException("Grid bots can only be instantited with exitTrigger of the type NO_EXIT")
        elif self.strategy.getName() == Strategies.GRID and self.stopLossType.getName() != StopLosses.NO_STOP:
            raise IncompatibleBotException("Grid bots should have stopLossType always set as NO_STOP")

    def getId(self):
        return self.id

    def getStrategy(self):
        return self.strategy

    def getTimeframe(self):
        return self.timeframe

    def hasBias(self):
        return self.biased

    def getStopLossType(self, value):
        return self.stopLossType

    def getExitTrigger(self, value):
        return self.exitTrigger

    def getMaxPyramiding(self, value):
        return self.maxPyramiding

    def getScore(self):
        return self.score

    def setScore(self, value):
        self.score = value

    def getUnrealisedBalance(self, value):
        return self.unrealisedBalance

    def setUnrealisedBalance(self, value):
        self.unrealisedBalance = value

    def getMaxUnrealisedLoss(self, value):
        return self.maxUnrealisedLoss

    def setMaxUnrealisedLoss(self, value):
        self.maxUnrealisedLoss = value

    def getMaxDrawdown(self, value):
        return self.maxDrawdown

    def setMaxDrawdown(self, value):
        self.maxDrawdown = value
