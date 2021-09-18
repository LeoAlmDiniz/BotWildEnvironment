
class MarketReaderConfigError(Exception):

    def __init__(self, message="Something went with Market Readers config"):
        self.message = message
        super().__init__(self.message)
