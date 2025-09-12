# file: spark/notebooks/lib/luis_gonzalez/account.py

class BankAccount:
    """A simple class to manage a bank account."""

    def __init__(self, initial_balance=0):
        """This is the constructor. It runs when you create a new BankAccount."""
        print(f"New account created with initial balance: ${initial_balance}")
        self.balance = initial_balance
             
        self.operations = {
            "deposit": self._deposit,
            "withdraw": self._withdraw,
            "get_balance": self._get_balance
        }

    def deposit(self, amount):
        """Adds money to the account."""
        if amount > 0:
            self.balance += amount
            print(f"Deposited: ${amount}. New balance: ${self.balance}")
        else:
            print("Error: Deposit amount must be positive.")

    def withdraw(self, amount):
        """Removes money from the account if funds are sufficient."""
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew: ${amount}. New balance: ${self.balance}")
        else:
            print(f"Error: Insufficient funds or invalid amount for withdrawal.")

    def get_balance(self):
        """Shows the current balance."""
        print(f"Current balance is: ${self.balance}")

    def process(self, operation_name, amount=None):
        """
        Dynamically executes an operation based on the provided string name.
        This is the main method you will call.
        """
        # Get the function from our dictionary using the operation_name key
        operation_to_run = self.operations.get(operation_name)

        if operation_to_run:
            if operation_name in ["deposit", "withdraw"]:
                if amount is not None:
                    operation_to_run(amount) 
                else:
                    print(f"Error: The '{operation_name}' operation requires an amount.")
            else:
                operation_to_run()
        else:
            print(f"Error: '{operation_name}' is not a valid operation.")