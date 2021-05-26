from datetime import datetime


class ParkingTicketMachine:
    def __init__(self):
        self.rate_per_hour = 5.0
        self.amount_inputted = None
        self.duration = None
        self.payment_type = "coin"
        self.is_using_coin = True
        self.current_time = None

    def insert_coin(self, amount):
        self.amount_inputted = amount
        self.current_time = datetime.now()

    def print(self):
        pass
