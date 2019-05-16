class InsufficientAmount(Exception):
    pass


class Wallet(object):
    
    def __init__(self, inital_amount=0):
        self.balance = inital_amount

    def spend_cash(self, amount):
        if self.balance < amount:
            raise InsufficientAmount('Not enough available to spend {}'.format(amount))
        self.balance -= amount

    def add_cash(self, amount):
        self.balance += amount