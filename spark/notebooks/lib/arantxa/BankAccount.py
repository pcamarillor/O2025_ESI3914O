class BankAccount:
    def __init__(self, initial_balance=0):
        self.balance = initial_balance
        self.operations = {
            "deposit": self.deposit,
            "withdraw": self.withdraw,
            "get_balance": self.get_balance,
            "transaction_history": self.transaction_history
        }
        self.transactions = []
        if initial_balance > 0:
            self.transactions.append(f"Initial deposit: ${initial_balance}")
    
    def deposit(self, amount):
        """Deposit money into the account"""
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self.balance += amount
        self.transactions.append(f"Deposit: ${amount}")
        return f"Deposited ${amount}. New balance: ${self.balance}"
    
    def withdraw(self, amount):
        """Withdraw money from the account"""
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount
        self.transactions.append(f"Withdrawal: ${amount}")
        return f"Withdrew ${amount}. New balance: ${self.balance}"
    
    def get_balance(self):
        """Get current account balance"""
        return f"Current balance: ${self.balance}"
    
    def transaction_history(self):
        """Get transaction history"""
        if not self.transactions:
            return "No transactions yet"
        return "\n".join(self.transactions)
    
    def process(self, operation_name, *args):
        """Dynamically execute an operation based on its name"""
        if operation_name not in self.operations:
            raise ValueError(f"Unknown operation: {operation_name}")
        
        operation = self.operations[operation_name]
        return operation(*args)
    
    def __str__(self):
        return f"BankAccount with balance: ${self.balance}"