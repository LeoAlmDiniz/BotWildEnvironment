from enum import Enum

from src.AssetsAndTimeframes.ITimeframeStrings import ITimeframeStrings


class BinanceTimeframeStrings(ITimeframeStrings):

    @staticmethod
    def tf5String():
        return "5m"

    @staticmethod
    def tf15String():
        return "15m"

    @staticmethod
    def tf30String():
        return "30m"

    @staticmethod
    def tf60String():
        return "1h"

    @staticmethod
    def tf240String():
        return "4h"

    @staticmethod
    def tfDString():
        return "1d"

    @staticmethod
    def tfWString():
        return "1w"

    @staticmethod
    def tfMString():
        return "1M"