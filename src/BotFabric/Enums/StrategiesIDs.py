from enum import Enum


class StrategiesIDs(Enum):
    RSIVWAP = "Rsi of Vwap"
    GRID = "Grid"
    MA = "Price is above one MA"
    MA2 = "2-Simple Moving Averages Cross"
    MA3 = "3-Simple Moving Averages Cross"

