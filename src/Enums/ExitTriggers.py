from enum import Enum


class ExitTriggers(Enum):
    NO_EXIT = 0  # Basicamente utilizado quando a mudanca de mao eh direta de long pra short
    STOPLOSS = 1
    REALISE_PROFIT = 2


