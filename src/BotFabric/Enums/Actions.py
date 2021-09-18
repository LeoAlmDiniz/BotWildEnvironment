from enum import Enum


class Actions(Enum):
    PASS = 0
    OPEN_LONG = 1
    OPEN_SHORT = 2
    CLOSE_LONG = 3
    CLOSE_SHORT = 4
    CLOSE_ANY = 5

