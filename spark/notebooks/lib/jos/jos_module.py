class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance
        self.operations = {
            "deposit": self.deposit,
            "withdraw": self.withdraw,
            "get_balance": self.get_balance
        }

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            return "Not enough money"
        self.balance -= amount
        return self.balance

    def get_balance(self):
        return self.balance

    def process(self, operation, *args):
        if operation in self.operations:
            return self.operations[operation](*args)
        else:
            return "Invalid operation"
