
class WebAddressError(Exception):

    def __init__(self, message="Something went wrong with Web Addresses trying to be accessed"):
        self.message = message
        super().__init__(self.message)
