import numpy as np


class WbeTechnicalAnalysis:

    @staticmethod
    def MA(period: int, dataset: list):
        np.nanmean(np.array(dataset))

    @staticmethod
    def EMA(period: int, dataset: list):
        np.nanmean(np.array(dataset))