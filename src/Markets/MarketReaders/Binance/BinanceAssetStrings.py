from enum import Enum

from src.AssetsAndTimeframes.IAssetStrings import IAssetStrings


class BinanceAssetStrings(IAssetStrings):

    @staticmethod
    def btc():
        return "btcusdt"