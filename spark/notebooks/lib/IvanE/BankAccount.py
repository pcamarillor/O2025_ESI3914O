class BankAccount:
    def __init__(self, initialBalance=0):
        self.balance = initialBalance  
        self.operations = {
            "deposit": self.deposit,
            "withdraw": self.withdraw,
            "get_balance": self.get_balance
        }

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self.balance:
            raise ValueError("Insufficient funds.")
        self.balance -= amount
        return self.balance

    def get_balance(self):
        return "Your current balance is: " + str(self.balance)

    def process(self, operation, *args):
        if operation not in self.operations:
            raise ValueError(f"Invalid operation: {operation}")
        return self.operations[operation](*args)
