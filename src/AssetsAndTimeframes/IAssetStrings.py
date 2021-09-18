import abc
from abc import ABC, abstractmethod


class IAssetStrings(ABC):

    @staticmethod
    @abstractmethod
    def btc():
        raise NotImplementedError
