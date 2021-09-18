from src.Markets.MarketIDs import MarketIDs


class Market:

    def __init__(self,
                 name: MarketIDs,
                 timeframe,
                 asset):
        self.name = name
        self.timeframe = timeframe
        self.asset = asset

