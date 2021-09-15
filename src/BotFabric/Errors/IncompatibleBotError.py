
class IncompatibleBotException(Exception):

    def __init__(self, message="Some combination of parameters in the declared bot is incompatible"):
        self.message = message
        super().__init__(self.message)
