import sys

from src.AssetsAndTimeframes.Assets import Assets
from src.AssetsAndTimeframes.Timeframes import Timeframes
from src.BotFabric.Bot import Bot
from src.BotFabric.ExitTriggers.NoExit import NoExit
from src.BotFabric.StopLosses.NoStop import NoStop
from src.BotFabric.Strategies.EMA import EMA
from src.BotFabric.Strategies.EMA2 import EMA2
from src.BotFabric.Strategies.EMA3 import EMA3
from src.BotFabric.Strategies.Grid import Grid
from src.BotFabric.Strategies.MA import MA
from src.BotFabric.Strategies.MA2 import MA2
from src.BotFabric.Strategies.MA3 import MA3
from src.Context.Assignment import Assignment
from src.Markets.MarketIDs import MarketIDs


def biasedGridBot(angle, biasStrategy) -> dict:
    return {
        "strategy": Grid(angle),
        "biased": True,
        "biasStrategy": biasStrategy,
        "stopLossType": NoStop(),
        "exitTrigger": NoExit(),
        "maxPyramiding": sys.maxsize
    }


def unbiasedGridBot() -> dict:
    return {
        "strategy": Grid(),
        "biased": True,
        "biasStrategy": None,
        "stopLossType": NoStop(),
        "exitTrigger": NoExit(),
        "maxPyramiding": sys.maxsize
    }


def binanceBTC(timeframe: Timeframes) -> dict:
    return {
        "market": MarketIDs.BINANCE,
        "asset": Assets.BTC,
        "timeframe": timeframe
    }


INITIAL_CONFIG = {
    ####################################################################################################################
    ################################################# GRID BOTS ########################################################
    ####################################################################################################################
    # CONVENTIONAL GRID BOT:
    unbiasedGridBot(): [binanceBTC(Timeframes.TF5)],
    # LONG TERM BIASED BOT:
    biasedGridBot(45, EMA(20)): [binanceBTC(Timeframes.TFW)],

    # SIMPLE MOVING AVERAGE GRIDS:
    biasedGridBot(30, MA()): [binanceBTC(Timeframes.TF5),
                              binanceBTC(Timeframes.TF15),
                              binanceBTC(Timeframes.TF30),
                              binanceBTC(Timeframes.TF60),
                              binanceBTC(Timeframes.TF240)],

    biasedGridBot(45, MA()): [binanceBTC(Timeframes.TF5),
                              binanceBTC(Timeframes.TF15),
                              binanceBTC(Timeframes.TF30),
                              binanceBTC(Timeframes.TF60),
                              binanceBTC(Timeframes.TF240)],

    biasedGridBot(60, MA()): [binanceBTC(Timeframes.TF5),
                              binanceBTC(Timeframes.TF15),
                              binanceBTC(Timeframes.TF30),
                              binanceBTC(Timeframes.TF60),
                              binanceBTC(Timeframes.TF240)],

    biasedGridBot(30, MA2()): [binanceBTC(Timeframes.TF5),
                               binanceBTC(Timeframes.TF15),
                               binanceBTC(Timeframes.TF30),
                               binanceBTC(Timeframes.TF60),
                               binanceBTC(Timeframes.TF240)],

    biasedGridBot(45, MA2()): [binanceBTC(Timeframes.TF5),
                               binanceBTC(Timeframes.TF15),
                               binanceBTC(Timeframes.TF30),
                               binanceBTC(Timeframes.TF60),
                               binanceBTC(Timeframes.TF240)],

    biasedGridBot(60, MA2()): [binanceBTC(Timeframes.TF5),
                               binanceBTC(Timeframes.TF15),
                               binanceBTC(Timeframes.TF30),
                               binanceBTC(Timeframes.TF60),
                               binanceBTC(Timeframes.TF240)],

    biasedGridBot(30, MA3()): [binanceBTC(Timeframes.TF5),
                               binanceBTC(Timeframes.TF15),
                               binanceBTC(Timeframes.TF30),
                               binanceBTC(Timeframes.TF60),
                               binanceBTC(Timeframes.TF240)],

    biasedGridBot(45, MA3()): [binanceBTC(Timeframes.TF5),
                               binanceBTC(Timeframes.TF15),
                               binanceBTC(Timeframes.TF30),
                               binanceBTC(Timeframes.TF60),
                               binanceBTC(Timeframes.TF240)],

    biasedGridBot(60, MA3()): [binanceBTC(Timeframes.TF5),
                               binanceBTC(Timeframes.TF15),
                               binanceBTC(Timeframes.TF30),
                               binanceBTC(Timeframes.TF60),
                               binanceBTC(Timeframes.TF240)],
    # EXPONENTIAL MOVING AVERAGE GRIDS:
    biasedGridBot(30, EMA()): [binanceBTC(Timeframes.TF5),
                               binanceBTC(Timeframes.TF15),
                               binanceBTC(Timeframes.TF30),
                               binanceBTC(Timeframes.TF60),
                               binanceBTC(Timeframes.TF240)],

    biasedGridBot(45, EMA()): [binanceBTC(Timeframes.TF5),
                               binanceBTC(Timeframes.TF15),
                               binanceBTC(Timeframes.TF30),
                               binanceBTC(Timeframes.TF60),
                               binanceBTC(Timeframes.TF240)],

    biasedGridBot(60, EMA()): [binanceBTC(Timeframes.TF5),
                               binanceBTC(Timeframes.TF15),
                               binanceBTC(Timeframes.TF30),
                               binanceBTC(Timeframes.TF60),
                               binanceBTC(Timeframes.TF240)],

    biasedGridBot(30, EMA2()): [binanceBTC(Timeframes.TF5),
                                binanceBTC(Timeframes.TF15),
                                binanceBTC(Timeframes.TF30),
                                binanceBTC(Timeframes.TF60),
                                binanceBTC(Timeframes.TF240)],

    biasedGridBot(45, EMA2()): [binanceBTC(Timeframes.TF5),
                                binanceBTC(Timeframes.TF15),
                                binanceBTC(Timeframes.TF30),
                                binanceBTC(Timeframes.TF60),
                                binanceBTC(Timeframes.TF240)],

    biasedGridBot(60, EMA2()): [binanceBTC(Timeframes.TF5),
                                binanceBTC(Timeframes.TF15),
                                binanceBTC(Timeframes.TF30),
                                binanceBTC(Timeframes.TF60),
                                binanceBTC(Timeframes.TF240)],

    biasedGridBot(30, EMA3()): [binanceBTC(Timeframes.TF5),
                                binanceBTC(Timeframes.TF15),
                                binanceBTC(Timeframes.TF30),
                                binanceBTC(Timeframes.TF60),
                                binanceBTC(Timeframes.TF240)],

    biasedGridBot(45, EMA3()): [binanceBTC(Timeframes.TF5),
                                binanceBTC(Timeframes.TF15),
                                binanceBTC(Timeframes.TF30),
                                binanceBTC(Timeframes.TF60),
                                binanceBTC(Timeframes.TF240)],

    biasedGridBot(60, EMA3()): [binanceBTC(Timeframes.TF5),
                                binanceBTC(Timeframes.TF15),
                                binanceBTC(Timeframes.TF30),
                                binanceBTC(Timeframes.TF60),
                                binanceBTC(Timeframes.TF240)]

    ####################################################################################################################
    ########################################### CONVENTIONAL BOTS ######################################################
    ####################################################################################################################
}


def getInitialConfig() -> list:
    output = []
    for botArgs, assignmentList in INITIAL_CONFIG:
        bot = Bot(strategy=botArgs["strategy"],
                  biased=botArgs["biased"],
                  biasStrategy=botArgs["biasStrategy"],
                  stopLossType=botArgs["stopLossType"],
                  exitTrigger=botArgs["exitTrigger"],
                  maxPyramiding=botArgs["maxPyramiding"])
        for assignmentArgs in assignmentList:
            assignment = Assignment(market=assignmentArgs["market"],
                                    asset=assignmentArgs["asset"],
                                    timeframe=assignmentArgs["timeframe"])
            bot.assign(assignment)
        output.append(bot)
    return output
