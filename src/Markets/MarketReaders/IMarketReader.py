from abc import ABC, abstractproperty, abstractmethod


class IMarketReader(ABC):

    @abstractmethod
    def connect(self):
        raise NotImplementedError
