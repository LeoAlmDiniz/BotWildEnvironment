from abc import ABC, abstractproperty, abstractmethod


class IExitTrigger(ABC):

    @abstractmethod
    def getName(self):
        raise NotImplementedError