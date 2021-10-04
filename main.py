import collections
from kline import Kline
from calculations import *
from transaction import Transaction

file_name = "AVAXUSDT-1m-2021-09.csv"

# 1440 1m candles fit in one day
previous_period_length = 1440

# my_list will contain 1-minute candle info from the last 24 hours
my_list = collections.deque([], previous_period_length)

# flag for currently in buy or sell mode
is_buying = False

# amounts of either currency in holdings
quote_amount = 100
base_amount = 0

# transactions made
transactions = []

with open(file_name, 'r') as f:

    # insert the first day of 1 minute candles to the list
    for i in range(previous_period_length):
        process_candle_data(f.readline(), my_list)

    # calculate highest and lowest seen price
    highest_price, highest_index, lowest_price, lowest_index = find_highest_and_lowest_price(my_list)

    # go through every 1-minute candle to see if it breaches highest/lowest price
    while True:
        file_line = f.readline()

        # if data_line is empty, reached end of file
        if not file_line:
            break

        # process the csv file line into the list
        process_candle_data(file_line, my_list)
        highest_index += 1
        lowest_index += 1

        # check if new candle exceeds highest price
        if my_list[0].high >= highest_price:
            highest_index = 0
            highest_price = my_list[0].high

            # sell logic
            if not is_buying:
                base_amount = sell(quote_amount, highest_price, transactions)


        # Else, check if new candle exceeds lowest price
        elif my_list[0].low <= lowest_price:
            lowest_index = 0
            lowest_price = my_list[0].low

            # buy logic
            if is_buying:


        # If the index exceeds list length, find the new highest/lowest index
        if highest_index >= previous_period_length or lowest_index >= previous_period_length:
            highest_price, highest_index, lowest_price, lowest_index = find_highest_and_lowest_price(my_list)

pass