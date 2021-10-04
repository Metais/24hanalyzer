

class Kline:
    """Class that stores and handles candle data"""

    def __init__(self, data_line):
        self.open_time = data_line[0]
        self.open = data_line[1]
        self.high = data_line[2]
        self.low = data_line[3]
        self.close = data_line[4]
        self.volume = data_line[5]
        self.close_time = data_line[6]
        self.quote_asset_volume = data_line[7]
        self.no_of_trades = data_line[8]

    def __str__(self):
        return str(self.open)
