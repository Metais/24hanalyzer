

class Transaction:
    """Class that stores transaction data. Fee is already priced in."""

    def __init__(self, is_buy, price, base_amount, quote_amount):
        self.is_buy = is_buy
        self.price = price
        self.base_amount = base_amount
        self.quote_amount = quote_amount
