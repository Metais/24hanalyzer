from datetime import datetime


class Transaction:
    """Class that stores transaction data. Fee is already priced in."""

    def __init__(self, is_buy, price, base_amount, date):
        self.is_buy = is_buy
        self.price = price
        self.base_amount = base_amount
        self.date = date

    def __str__(self):
        return f'{datetime.utcfromtimestamp(self.date/1000).strftime("%Y-%m-%d %H:%M:%S")} - ' \
               f'{"Buy" if self.is_buy else "Sell"}: {self.base_amount} at price {self.price}'
