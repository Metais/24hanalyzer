import math
from kline import Kline
from transaction import Transaction


def find_highest_and_lowest_price(klines):
    """Finds the highest and lowest price in an input of klines.
        Returns the highest price and the lowest price in that order, as well as its index."""

    highest_price = -1
    lowest_price = math.inf

    highest_index = -1
    lowest_index = -1

    for i, kline in enumerate(klines):
        if kline.high > highest_price:
            highest_price = kline.high
            highest_index = i
        if kline.low < lowest_price:
            lowest_price = kline.low
            lowest_index = i

    return highest_price, highest_index, lowest_price, lowest_index


def process_candle_data(data_line, my_list):
    """Processes the raw csv line into a kline object, added to my_list"""

    # process the line in the csv file into a list of floats
    data_line = [float(x) for x in data_line.strip().split(',')][:-3]

    # transform list of floats to a kline object and append to FIFO
    my_list.appendleft(Kline(data_line))


def sell(quote_amount, price, transactions):
    # calculate received amount by subtracting 0.1% fee cost
    base_amount = price * quote_amount * 0.999

    transactions.append(Transaction(False, price, base_amount))
