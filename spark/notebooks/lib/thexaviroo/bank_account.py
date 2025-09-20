# Re-Added for generate_schema on Sep 18
class BankAccount:
    def __init__(self, initial_balance=0):
        self.balance = initial_balance
        self.operations = {
            "deposit": self._deposit,
            "withdraw": self._withdraw,
            "get_balance": self._get_balance
        }

    def _deposit(self, amount):
        self.balance += amount
        return f"Deposited {amount}. New balance: {self.balance}"

    def _withdraw(self, amount):
        if amount > self.balance:
            return f"Insufficient funds. Current balance: {self.balance}"
        self.balance -= amount
        return f"Withdrew {amount}. New balance: {self.balance}"

    def _get_balance(self, _=None):
        return f"Current balance: {self.balance}"

    def process(self, operation_name, amount=None):
        if operation_name in self.operations:
            return self.operations[operation_name](amount)
        return f"Operation '{operation_name}' not recognized."
