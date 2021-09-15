# <streamName> should always be set as "<symbol>@kline_<interval>"
# where <symbol> is for instance "btcusdt" and <interval> is for example "5m"
# thus, assetList and timeframeList should be fed with the respective Enums that return these strings

# When there's only one stream to be collected
# there's only one address ws address should be:  /ws/<streamName>

# When there are multiple streams to be collected:
# there are multiple streams we want to collect data from, and in this case the ws adress should be
# /stream?streams=<streamName1>/<streamName2>/<streamName3>


from src.MarketReaders.Errors.MarketReaderConfigError import MarketReaderConfigError
from src.MarketReaders.IMarketReader import IMarketReader


class BinanceMarketReader(IMarketReader):

    def __init__(self, assetList: list, timeframeList: list):
        self.socket = "wss://stream.binance.com:9443"
        self.assetList = assetList
        self.timeframeList = timeframeList
        if len(self.assetList) * len(self.timeframeList) <= 0:
            raise MarketReaderConfigError("You need to config BinanceMarketReader to collect data from at least "
                                          + "one Asset in at least one timeframe")

    def getAddress(self):
        if len(self.assetList) * len(self.timeframeList) == 1:
            streamName = self.assetList[0] + "@kline_" + self.timeframeList[0]
            return self.socket + "/ws/" + streamName
        else:
            address = self.socket + "/stream?streams="
            for a in range(len(self.assetList)):
                for t in range(len(self.timeframeList)):
                    if a != 0 and t != 0:
                        address += "/"
                    streamName = self.assetList[a] + "@kline_" + self.timeframeList[t]
                    address += streamName
