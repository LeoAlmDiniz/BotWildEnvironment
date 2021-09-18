import abc
from abc import ABC, abstractmethod


class ITimeframeStrings(ABC):

    @staticmethod
    @abstractmethod
    def tf5String():
        raise NotImplementedError

    @staticmethod
    @abstractmethod
    def tf15String():
        raise NotImplementedError

    @staticmethod
    @abstractmethod
    def tf30String():
        raise NotImplementedError

    @staticmethod
    @abstractmethod
    def tf60String():
        raise NotImplementedError

    @staticmethod
    @abstractmethod
    def tf240String():
        raise NotImplementedError

    @staticmethod
    @abstractmethod
    def tfDString():
        raise NotImplementedError

    @staticmethod
    @abstractmethod
    def tfWString():
        raise NotImplementedError

    @staticmethod
    @abstractmethod
    def tfMString():
        raise NotImplementedError