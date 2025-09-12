import math

class BankAccount:
    def __init__(self, initial_balance=0):
        self.balance = initial_balance
    
        self.operations = {
            "deposit": self.deposit,
            "withdraw": self.withdraw,
            "get_balance": self.get_balance
        }

    def deposit(self, amount):
        self.balance += amount
        return f"Deposited {amount}, new balance: {self.balance}"

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient funds"
        self.balance -= amount
        return f"Withdrew {amount}, new balance: {self.balance}"

    def get_balance(self):
        return f"Current balance: {self.balance}"

 
