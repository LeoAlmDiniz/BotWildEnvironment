from src.AssetsAndTimeframes.ITimeframeStrings import GlobalTimeframes
from src.BotFabric.ExitTriggers.NoExit import NoExit
from src.BotFabric.StopLosses.NoStop import NoStop
from src.BotFabric.Strategies.Grid import Grid
from src.BotFabric.Strategies.MA3 import MA3


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
        "timeframe": GlobalTimeframes.TD5,
        "biasStrategy": None,
        "biased": True,
        "stopLossType": NoStop(),
        "exitTrigger": NoExit()}


INITIAL_CONFIG = [
    biasedGridBot(30, GlobalTimeframes.TF15, MA3(), 10000),
    biasedGridBot(30, GlobalTimeframes.TF60, MA3(), 10000),
    biasedGridBot(30, GlobalTimeframes.TF240, MA3(), 10000),
    biasedGridBot(30, GlobalTimeframes.TFD, MA3(), 10000),
    biasedGridBot(45, GlobalTimeframes.TF15, MA3(), 10000),
    biasedGridBot(45, GlobalTimeframes.TF60, MA3(), 10000),
    biasedGridBot(45, GlobalTimeframes.TF240, MA3(), 10000),
    biasedGridBot(45, GlobalTimeframes.TFD, MA3(), 10000),
    biasedGridBot(60, GlobalTimeframes.TF15, MA3(), 10000),
    biasedGridBot(60, GlobalTimeframes.TF60, MA3(), 10000),
    biasedGridBot(60, GlobalTimeframes.TF240, MA3(), 10000),
    biasedGridBot(60, GlobalTimeframes.TFD, MA3(), 10000),
    unbiasedGridBot(10000)

]
