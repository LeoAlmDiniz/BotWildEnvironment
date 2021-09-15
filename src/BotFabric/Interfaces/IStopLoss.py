from abc import ABC, abstractproperty, abstractmethod


class IStopLoss(ABC):

    @abstractmethod
    def getName(self):
        raise NotImplementedError

    @abstractmethod
    def getGap(self):
        raise NotImplementedError
