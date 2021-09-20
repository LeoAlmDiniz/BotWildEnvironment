from src.Context import ContextConfig0


class WBEContext:

    def __init__(self, resetContext):
        self.bots = []
        #Bot => [MARKET, ASSET, TF]
        if resetContext:
            self.bots = ContextConfig0.getInitialConfig()
        else:
            self.recoverBotsInMarkets()

    def run(self):
        pass

    def recoverBotsInMarkets(self):
        pass

    def resetActiveBotsState(self):
        pass

    def recoverActiveBotsState(self):
        pass

    def createMarketReaders(self):
        assetList = []
        timeframeList = []
        for bot_guid in self.activeBots.inventory:
            assetList.append(self.activeBots.getBotById(bot_guid).asset)
            timeframeList.append(self.activeBots.getBotById(bot_guid).timeframe)


