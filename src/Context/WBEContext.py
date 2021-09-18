from src.Context.ActiveBots import ActiveBots


class WBEContext:

    def __init__(self, resetContext):
        self.activeBots = ActiveBots()
        self.marketReaders = {}
        if resetContext:
            self.resetActiveBots()
        else:
            self.recoverActiveBots()

    def run(self):
        pass

    def recoverActiveBots(self):
        # we will keep a backup of ActiveBots through pickle module
        pass

    def resetActiveBots(self):
        pass

    def createMarketReaders(self):
        assetList = []
        timeframeList = []
        for bot_guid in self.activeBots.inventory:
            assetList.append(self.activeBots.getBotById(bot_guid).asset)
            timeframeList.append(self.activeBots.getBotById(bot_guid).timeframe)


