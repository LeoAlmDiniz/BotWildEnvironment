from src.Markets.MarketReaders.IMarketReader import IMarketReader


class ActiveBots:

    def __init__(self):
        self.list = []

    def createMarketReader(self, marketReader: IMarketReader):
        self.list.append(marketReader)

