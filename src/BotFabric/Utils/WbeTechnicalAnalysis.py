import numpy as np


class WbeTechnicalAnalysis:

    @staticmethod
    def crossover(over: float, over0: float, under: float, under0: float) -> bool:
        return over0 < under0 and over > under

    @staticmethod
    def crossunder(under: float, under0: float, over: float, over0: float) -> bool:
        return under0 > over0 and under < over

    @staticmethod
    def MA(period: int, dataset: list):
        np.nanmean(np.array(dataset[0:period]))

    @staticmethod
    def EMA(period: int, dataset: list):
        np.nanmean(np.array(dataset))