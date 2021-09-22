from src.BotFabric.Bot import Bot


class IncompatibleBotException(Exception):

    def __init__(self, bot: Bot, message="Some combination of parameters in the declared bot is incompatible"):
        self.message = message + "\n"
        self.message += "#########################################" + "\n"
        self.message += "############### BOT REPORT ##############" + "\n"
        self.message += "#########################################" + "\n"
        self.message += "# Strategy: "      + str(bot.strategy.getName().value) + "\n"
        self.message += "# Biased?: "       + str(bot.biased) + "\n"
        self.message += "# Bias Strategy: " + str(bot.strategy.biasStrategy.getName().value) + "\n"
        self.message += "# Stop Loss type: "+ str(bot.stopLossType.getName().value) + "\n"
        self.message += "# Exit Trigger: "  + str(bot.exitTrigger.getName().value) + "\n"
        self.message += "# Max Pyramiding: "+ str(bot.maxPyramiding) + "\n"
        self.message += "#########################################"
        super().__init__(self.message)
