from src.BotFabric.ExitTriggers.NoExit import NoExit
from src.BotFabric.StopLosses.NoStop import NoStop
from src.BotFabric.Strategies.Grid import Grid
from src.BotFabric.Strategies.MA3 import MA3

from src.Enums.Timeframes import Timeframes


def biasedGridBot(angle, timeframe, biasStrategy, maxPyramiding):
    return {
        "timeframe": timeframe,
        "biasStrategy": biasStrategy,
        "maxPyramiding": maxPyramiding,
        ###constants###
        "strategy": Grid(angle),
        "biased": True,
        "stopLossType": NoStop(),
        "exitTrigger": NoExit()}


def unbiasedGridBot(maxPyramiding):
    return {
        "maxPyramiding": maxPyramiding,
        ###constants###
        "strategy": Grid(),
        "timeframe": Timeframes.TD5,
        "biasStrategy": None,
        "biased": True,
        "stopLossType": NoStop(),
        "exitTrigger": NoExit()}


INITIAL_CONFIG = [

    biasedGridBot(30, Timeframes.TF15, MA3(), 10000),
    biasedGridBot(30, Timeframes.TF60, MA3(), 10000),
    biasedGridBot(30, Timeframes.TF240, MA3(), 10000),
    biasedGridBot(30, Timeframes.TFD, MA3(), 10000),

    biasedGridBot(45, Timeframes.TF15, MA3(), 10000),
    biasedGridBot(45, Timeframes.TF60, MA3(), 10000),
    biasedGridBot(45, Timeframes.TF240, MA3(), 10000),
    biasedGridBot(45, Timeframes.TFD, MA3(), 10000),

    biasedGridBot(60, Timeframes.TF15, MA3(), 10000),
    biasedGridBot(60, Timeframes.TF60, MA3(), 10000),
    biasedGridBot(60, Timeframes.TF240, MA3(), 10000),
    biasedGridBot(60, Timeframes.TFD, MA3(), 10000),

    unbiasedGridBot(10000)

]
