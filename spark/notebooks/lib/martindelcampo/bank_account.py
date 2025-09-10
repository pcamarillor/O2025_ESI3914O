class BankAccount:
    def __init__(self, initial_balance=0.0):
        self.balance = float(initial_balance)       # Set the starting balance as a float
        self.ops = {                                # Dictionary mapping operation names to methods
            "deposit": self.deposit,
            "withdraw": self.withdraw,
            "get_balance": self.get_balance,
        }

    def process(self, op, *args):                   # op: a string with the operation name ("deposit", "withdraw", or "get_balance") *args: additional arguments needed for the operation (e.g., amount for deposit/withdraw)
        if op not in self.ops:                      # Check if the operation is valid
            raise ValueError("Unknown operation")
        return self.ops[op](*args)                  # Call the corresponding method with arguments

    def deposit(self, amount):
        a = float(amount)                           # Convert amount to float
        if a <= 0:                                  # Check for positive amount
            raise ValueError("Amount must be > 0")
        self.balance += a                           # Add amount to balance
        return self.balance                         # Return new balance

    def withdraw(self, amount):
        a = float(amount)                           # Convert amount to float
        if a <= 0:                                  # Check for positive amount
            raise ValueError("Amount must be > 0")
        if a > self.balance:                        # Check for sufficient funds
            raise ValueError("Insufficient funds")
        self.balance -= a                           # Subtract amount from balance
        return self.balance                         # Return new balance

    def get_balance(self):
        return self.balance                         # Return current balance