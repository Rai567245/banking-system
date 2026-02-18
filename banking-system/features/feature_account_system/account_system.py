class Account:
    def __init__(self, acc_num, name, balance, pin, status):
        self.acc_num = acc_num
        self.name = name
        self.balance = float(balance)
        self.pin = pin
        self.status = status
        self.pin_attempts = 0

    def is_active(self):
        return self.status == "Active"
    
    def block_account(self):
        self.status == "Blocked"