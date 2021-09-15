from src.BotFabric.Bot import Bot


class ActiveBots:

    def __init__(self):
        self.inventory = {}

    def createBot(self, bot: Bot):
        self.inventory[bot.id] = bot
