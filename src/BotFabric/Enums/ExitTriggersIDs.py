from enum import Enum


class ExitTriggersIDs(Enum):
    NO_EXIT = "Always operating"  # Basicamente utilizado quando a mudanca de mao eh direta de long pra short
    STOPLOSS = "Exits based on stop loss (should be combined with trailing stop)"
    REALISE_PROFIT = "Exits based on profit level"
    STOP_OR_REALISE = "Exits based either on profit level or stop loss"

