# <streamName> should always be set as "<symbol>@kline_<interval>"
# where <symbol> is for instance "btcusdt" and <interval> is for example "5m"
# thus, assetList and timeframeList should be fed with the respective Enums that return these strings

# When there's only one stream to be collected
# there's only one address ws address should be:  /ws/<streamName>

# When there are multiple streams to be collected:
# there are multiple streams we want to collect data from, and in this case the ws adress should be
# /stream?streams=<streamName1>/<streamName2>/<streamName3>
import websocket

from src.Markets.MarketReaders.Errors.MarketReaderConfigError import MarketReaderConfigError
from src.Markets.MarketReaders.IMarketReader import IMarketReader


class BinanceMarketReader(IMarketReader):

    def __init__(self, assetList: list, timeframeList: list):
        self.socket = "wss://stream.binance.com:9443"
        self.assetList = assetList
        self.timeframeList = timeframeList
        if len(self.assetList) * len(self.timeframeList) <= 0:
            raise MarketReaderConfigError("You need to config BinanceMarketReader to collect data from at least "
                                          + "one Asset in at least one timeframe")
        self.ws = websocket.WebSocketApp(self.address(),
                                         on_open=self.onOpen,
                                         on_close=self.onClose,
                                         on_message=self.onMessage)

    def address(self) -> str:
        if len(self.assetList) * len(self.timeframeList) == 1:
            streamName = self.assetList[0].value + "@kline_" + self.timeframeList[0].value
            address = self.socket + "/ws/" + streamName
        else:
            address = self.socket + "/stream?streams="
            for a in range(len(self.assetList)):
                for t in range(len(self.timeframeList)):
                    if a != 0 and t != 0:
                        address += "/"
                    streamName = self.assetList[a].value + "@kline_" + self.timeframeList[t].value
                    address += streamName
        return address

    def connect(self):
        self.ws.run_forever()

    @staticmethod
    def onOpen(ws):
        print("Openned connection")

    @staticmethod
    def onClose(ws):
        print("Closed connection")

    @staticmethod
    def onMessage(ws, message):
        print("Received message")




