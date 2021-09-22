from enum import Enum


class StopLossesIDs(Enum):
    NO_STOP = "NO_STOP"
    UNTRAILING_STOP = "FIXED STOP LOSS"
    TRAILING_STOP = "TRAILING STOP LOSS"


