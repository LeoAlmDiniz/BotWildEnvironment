from abc import ABC, abstractmethod


class IBot(ABC):

    @abstractmethod
    def getId(self):
        raise NotImplementedError

    @abstractmethod
    def getStrategy(self):
        raise NotImplementedError

    @abstractmethod
    def getTimeframe(self):
        raise NotImplementedError

    @abstractmethod
    def hasBias(self, value):
        raise NotImplementedError

    @abstractmethod
    def getStopLossType(self, value):
        raise NotImplementedError

    @abstractmethod
    def getExitTrigger(self, value):
        raise NotImplementedError

    @abstractmethod
    def getMaxPyramiding(self, value):
        raise NotImplementedError

    @abstractmethod
    def getScore(self):
        raise NotImplementedError

    @abstractmethod
    def setScore(self, value):
        raise NotImplementedError

    @abstractmethod
    def getUnrealisedBalance(self, value):
        raise NotImplementedError

    @abstractmethod
    def setUnrealisedBalance(self, value):
        raise NotImplementedError

    @abstractmethod
    def getMaxUnrealisedLoss(self, value):
        raise NotImplementedError

    @abstractmethod
    def setMaxUnrealisedLoss(self, value):
        raise NotImplementedError

    @abstractmethod
    def getMaxDrawdown(self, value):
        raise NotImplementedError

    @abstractmethod
    def getMaxDrawdown(self, value):
        raise NotImplementedError

    @abstractmethod
    def setMaxDrawdown(self, value):
        raise NotImplementedError
