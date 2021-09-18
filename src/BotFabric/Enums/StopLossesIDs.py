from enum import Enum


class StopLossesIDs(Enum):
    NO_STOP = "No stop loss"
    UNTRAILING_STOP = "Fixed stop loss"
    TRAILING_STOP = "Moving stop loss"


