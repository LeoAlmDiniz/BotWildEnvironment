from typing import Union

from numpy import NaN

from src.BotFabric.Enums.Actions import Actions
from src.BotFabric.Enums.ExitTriggersIDs import ExitTriggersIDs
from src.BotFabric.Enums.Biases import Biases
from src.BotFabric.Enums.Orders import Orders
from src.BotFabric.Enums.StopLossesIDs import StopLossesIDs
from src.BotFabric.Enums.StrategiesIDs import StrategiesIDs
from src.BotFabric.Errors.IncompatibleBotError import IncompatibleBotException
from src.BotFabric.Interfaces.IStopLoss import IStopLoss
from src.BotFabric.Interfaces.IStrategy import IStrategy
from src.BotFabric.Interfaces.IExitTrigger import IExitTrigger
import uuid
from src.Context.Assignment import Assignment


class Bot:

    def __init__(self, strategy: IStrategy,
                 biased: bool,
                 biasStrategy: Union[None, IStrategy],
                 stopLossType: IStopLoss,
                 exitTrigger: IExitTrigger,
                 maxPyramiding: int):
        # BLUEPRINT
        self.guid = uuid.uuid4()
        self.strategy = strategy
        self.biased = biased  # LER OBSERVACAO 1
        if self.biased:
            self.strategy.setBiasStrategy(biasStrategy)
        self.stopLossType = stopLossType
        self.exitTrigger = exitTrigger
        self.maxPyramiding = maxPyramiding
        self.assignmentList = []

        # OPERATION
        self.dataset = [NaN] * max(strategy.longestPeriod(), biasStrategy.longestPeriod())
        self.orderCount = 0
        self.action = Actions.PASS

        # SCORE
        self.score = 0
        self.unrealisedBalance = 0
        self.maxUnrealisedLoss = 0
        self.maxDrawdown = 0

        # ERROR TREATMENT
        self.applyRestrictions()

    # BLUEPRINT

    def datasetSize(self) -> int:
        return len(self.dataset)

    def assign(self, assignment: Assignment):
        self.assignmentList.append(assignment)

    # OPERATION

    def update(self, value: Union[float, None]):
        self.dataset.insert(0, value)
        self.dataset.pop()
        self.strategy.update(self.dataset)
        if self.biased:
            self.strategy.biasStrategy.update(self.dataset)

    # SCORE

    def getScore(self) -> float:
        return self.score

    def setScore(self, value: float):
        self.score = value

    def getUnrealisedBalance(self) -> float:
        return self.unrealisedBalance

    def setUnrealisedBalance(self, value: float):
        self.unrealisedBalance = value

    def getMaxUnrealisedLoss(self) -> float:
        return self.maxUnrealisedLoss

    def setMaxUnrealisedLoss(self, value: float):
        self.maxUnrealisedLoss = value

    def getMaxDrawdown(self) -> float:
        return self.maxDrawdown

    def setMaxDrawdown(self, value: float):
        self.maxDrawdown = value

    # ERROR TREATMENT

    def applyRestrictions(self):
        if self.strategy is None:
            raise IncompatibleBotException(self, "Cannot create a Bot without strategy")
        if self.biased and self.strategy.biasStrategy is None:
            raise IncompatibleBotException(self, "Cannot create a biased Bot without biasStrategy")
        if self.strategy.getName() == StrategiesIDs.GRID and self.exitTrigger.getName() != ExitTriggersIDs.NO_EXIT:
            raise IncompatibleBotException(self,
                                           "Grid bots can only be instantiated with exitTrigger of the type NO_EXIT")
        if self.strategy.getName() == StrategiesIDs.GRID and self.stopLossType.getName() != StopLossesIDs.NO_STOP:
            raise IncompatibleBotException(self, "Grid bots should have stopLossType always set as NO_STOP")

# OBSERVACAO 1: BOTS biased=true e BOTS biased=false

# Sao dois tipos de bots de operacao diferentes. Bots biased=true (bots que assumem vies) usam alguma metodologia
# externa a sua estrategia de trade para avaliar se o mercado esta em tendencia de alta (bull), tendencia de baixa
# (bear) ou lateralizado (crab). A partir desta avaliacao preliminar (biasStrategy) ele soh assume posicoes longs
# (entrada e saida) caso o mercado esteja bull; similarmente, short para bear, mas assume os dois tipos de operacao
# caso acredite que o mercado esta crab. Nao eh necessario que a biasStrategy o faca assumir as 3 posicoes,
# mas pelo menos BULL e BEAR sim. Caso tipico que exemplifica isso tudo eh a famosa MACD EMA 200 Strategy. Soh
# longa se o preco estiver acima de EMA 200, soh shorta se ele estiver abaixo.

# Bots biased=false, obviamente, nao contem uma biasStrategy e so assumem posicoes long/short de acordo com o que
# a trading strategy diz. Isso nao significa que esses bots estejam com operacao aberta sempre, uma vez que estrategias
# que permitam posicao CRAB vao fazer com que o bot apenas feche uma operacao sem abrir outra.
