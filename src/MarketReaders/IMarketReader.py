from abc import ABC, abstractproperty, abstractmethod


class IMarketReader(ABC):

    @abstractmethod
    def getAddress(self):
        raise NotImplementedError
