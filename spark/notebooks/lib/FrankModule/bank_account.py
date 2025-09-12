class BankAccount:
    def __init__(self, initial_balance=0):
        self.balance = initial_balance
        # Diccionario que mapea nombres a funciones
        self.operations = {
            "deposit": self.deposit,
            "withdraw": self.withdraw,
            "get_balance": self.get_balance
        }

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("El depósito debe ser mayor a 0")
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("El retiro debe ser mayor a 0")
        if amount > self.balance:
            raise ValueError("Fondos insuficientes")
        self.balance -= amount
        return self.balance

    def get_balance(self):
        return self.balance

    def process(self, operation, *args):
        if operation not in self.operations:
            raise ValueError(f"Operación no válida: {operation}")
        return self.operations[operation](*args)
