from src.AssetsAndTimeframes.Assets import Assets
from src.AssetsAndTimeframes.Timeframes import Timeframes
from src.Markets.MarketIDs import MarketIDs


class Assignment:

    def __init__(self,
                 market: MarketIDs,
                 asset: Assets,
                 timeframe: Timeframes):
        self.market = market
        self.asset = asset
        self.timeframe = timeframe
