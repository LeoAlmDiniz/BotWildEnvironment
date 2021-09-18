import numpy as np
from src.BotFabric.Enums.StrategiesIDs import StrategiesIDs
from src.BotFabric.Interfaces.IStrategy import IStrategy


class Grid(IStrategy):

    def __init__(self, angle=0):
        self.name = StrategiesIDs.GRID
        self.biasModifier = float(np.invert(np.cos(np.deg2rad(angle))))

    def getName(self):
        return self.name

    def longestPeriod(self):
        return 1
