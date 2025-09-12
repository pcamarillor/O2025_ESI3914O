class BankAccount:
    def __init__(self, initial_balance=0):
        """
        Initialize the bank account with an initial balance.
        """
        self._balance = initial_balance
        
        #   Create dictionary mapping operation names to function references
        # This demonstrates functional programming by storing function pointers
        self._operations = {
            "deposit": self._deposit,
            "withdraw": self._withdraw,
            "get_balance": self._get_balance,
            "check_balance": self._get_balance,  # Alternative name for same operation
            "transfer": self._transfer,
            "add_interest": self._add_interest
        }
    
    def _deposit(self, amount):
        """
        Private method to handle deposit operations.
        """
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        
        self._balance += amount
        return f"Deposited ${amount:.2f}. New balance: ${self._balance:.2f}"
    
    def _withdraw(self, amount):
        """
        Private method to handle withdrawal operations.
        """
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        
        if amount > self._balance:
            raise ValueError("Insufficient funds")
        
        self._balance -= amount
        return f"Withdrew ${amount:.2f}. New balance: ${self._balance:.2f}"
    
    def _get_balance(self):
        """
        Private method to return current balance.
        """
        return f"Current balance: ${self._balance:.2f}"
    
    def _transfer(self, amount, target_account):
        """
        Private method to transfer money to another account.
        """
        if not isinstance(target_account, BankAccount):
            raise TypeError("Target must be a BankAccount instance")
        
        # Withdraw from this account
        self._withdraw(amount)
        # Deposit to target account
        target_account._deposit(amount)
        return f"Transferred ${amount:.2f}. Your new balance: ${self._balance:.2f}"
    
    def _add_interest(self, rate):
        """
        Private method to add interest to the account.
        """
        if rate < 0:
            raise ValueError("Interest rate cannot be negative")
        
        interest = self._balance * (rate / 100)
        self._balance += interest
        return f"Added {rate}% interest (${interest:.2f}). New balance: ${self._balance:.2f}"
    
    def process(self, operation, *args, **kwargs):
        """
        Dynamic operation processor that executes functions based on string keys.
        """
        # Validate that the requested operation exists
        if operation not in self._operations:
            available_ops = ", ".join(self._operations.keys())
            raise ValueError(f"Unknown operation '{operation}'. Available operations: {available_ops}")
        
        # Dynamically retrieve and execute the function
        operation_function = self._operations[operation]
        
        try:
            # Step 11: Execute the function with provided arguments
            result = operation_function(*args, **kwargs)
            return result
        except Exception as e:
            return f"Error executing '{operation}': {str(e)}"
    
    def get_available_operations(self):
        """
        Return list of available operations.
        """
        return list(self._operations.keys())