from src.OutputModels.ActiveBots import ActiveBots


class WBEContext:

    def __init__(self, resetContext):
        self.activeBots = ActiveBots()
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
    
