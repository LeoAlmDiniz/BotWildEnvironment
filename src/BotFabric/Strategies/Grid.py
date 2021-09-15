import numpy as np
from src.Enums.Strategies import Strategies
from src.BotFabric.Interfaces.IStrategy import IStrategy


class Grid(IStrategy):

    def __init__(self, angle=0):
        self.name = Strategies.GRID
        self.biasModifier = float(np.invert(np.cos(np.deg2rad(angle))))

    def getName(self):
        return self.name
