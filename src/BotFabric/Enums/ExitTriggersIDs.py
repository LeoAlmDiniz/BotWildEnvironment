from enum import Enum


class ExitTriggersIDs(Enum):
    NO_EXIT = "NO EXIT"  # Basicamente utilizado quando a mudanca de mao eh direta de long pra short
    STOPLOSS = "TOUCHING STOP LOSS"
    REALISE_PROFIT = "ACHIEVING CERTAIN PROFIT"
    STOP_OR_REALISE = "EITHER TOUCHING STOP LOSS OR ACHIEVING CERTAIN PROFIT"

