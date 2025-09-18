class BankAccount:
    def __init__(self, initial_balance=0):
        self._balance = initial_balance
        self._operations = {
            "deposit": self._deposit,
            "withdraw": self._withdraw,
            "get_balance": self._get_balance
        }

    def _deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be greater than zero.")
        self._balance += amount
        return f"Deposit successful. New balance: ${self._balance}"

    def _withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be greater than zero.")
        if amount > self._balance:
            raise ValueError("Insufficient funds.")
        self._balance -= amount
        return f"Withdrawal successful. New balance: ${self._balance}"

    def _get_balance(self, *_):
        return f"Current balance: ${self._balance}"

    def process(self, operation_name, amount=None):
        operation = self._operations.get(operation_name)
        if not operation:
            raise ValueError(f"Invalid operation: '{operation_name}'")
        return operation(amount) if amount is not None else operation()

