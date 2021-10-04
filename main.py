import collections
from calculations import *

file_name = "data/AVAXUSDT-1m-2021-01.csv"

# 1440 1m candles fit in one day
previous_period_length = 1440

# how many minutes to wait for a buy/sell
minute_wait_time = 10

# my_list will contain 1-minute candle info from the last 24 hours
my_list = collections.deque([], previous_period_length)

# flag for currently in buy or sell mode
is_buying = False

# amounts of either currency in holdings
base_amount = 100
quote_amount = 0

# transactions made
transactions = []

# counter to time a buy/sell
counter = 0

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

        # check if minute_wait counter finished countdown, if so, execute a buy/sell order
        if counter > 0:
            counter -= 1
            if counter == 0:
                if not is_buying:
                    base_amount, quote_amount = sell(base_amount, highest_price, my_list[0].open_time, transactions)
                    is_buying = True
                else:
                    base_amount, quote_amount = buy(quote_amount, lowest_price, my_list[0].open_time, transactions)
                    is_buying = False

        # check if new candle exceeds highest price
        if my_list[0].high >= highest_price:
            highest_index = 0
            highest_price = my_list[0].high

            # sell logic
            if not is_buying and counter == 0:
                counter = minute_wait_time

        # else, check if new candle exceeds lowest price
        elif my_list[0].low <= lowest_price:
            lowest_index = 0
            lowest_price = my_list[0].low

            # buy logic
            if is_buying and counter == 0:
                counter = minute_wait_time

        # if the index exceeds list length, find the new highest/lowest index
        if highest_index >= previous_period_length or lowest_index >= previous_period_length:
            highest_price, highest_index, lowest_price, lowest_index = find_highest_and_lowest_price(my_list)

pass