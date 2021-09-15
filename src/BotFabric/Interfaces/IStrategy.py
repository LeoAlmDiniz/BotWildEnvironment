from abc import ABC, abstractproperty, abstractmethod


class IStrategy(ABC):

    @abstractmethod
    def getName(self):
        raise NotImplementedError



