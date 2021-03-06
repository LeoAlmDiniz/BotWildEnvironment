from src.AssetsAndTimeframes.Assets import Assets
from src.AssetsAndTimeframes.Timeframes import Timeframes
from src.Markets.MarketIDs import MarketIDs


class Market:

    def __init__(self,
                 name: MarketIDs,
                 timeframe: Timeframes,
                 asset: Assets):
        self.name = name
        self.timeframe = timeframe
        self.asset = asset

