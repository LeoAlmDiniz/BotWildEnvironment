import sys
import numpy as np
from numpy import NaN


def main(resetContext=True):
    # ctx = WBEContext(resetContext)
    # ctx.run()
    # a = MarketReaderIDs.BINANCE
    # b = MarketReaderIDs.BINANCE
    # print(a == b)
    list = [NaN] * 200
    list.insert(0, 256)
    list.pop()
    # print(np.array(filter(None, list)))
    print(list)
    print(np.nanmean(np.array(list)))
    # print(np.array(list).mean())


if __name__ == '__main__':
    main()
