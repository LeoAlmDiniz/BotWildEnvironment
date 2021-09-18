import uuid

from src.BotFabric.Bot import Bot


class ActiveBots:

    def __init__(self):
        self.inventory = {}

    def createBot(self, bot: Bot):
        self.inventory[bot.guid] = bot

    def getBotById(self, guid: uuid) -> Bot:
        return self.inventory[guid]