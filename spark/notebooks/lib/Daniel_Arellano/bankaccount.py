class BankAccount:
    def __init__(self, initial_balance=0):
        self.balance = initial_balance

        # Operaciones disponibles
        self.operations = {
            "deposit": self._deposit,
            "withdraw": self._withdraw,
            "get_balance": self._get_balance
        }

    def _deposit(self, amount):
        if amount <= 0:
            raise ValueError("El depósito debe ser mayor a 0")
        self.balance += amount
        return self.balance

    def _withdraw(self, amount):
        if amount <= 0:
            raise ValueError("El retiro debe ser mayor a 0")
        if amount > self.balance:
            raise ValueError("Fondos insuficientes")
        self.balance -= amount
        return self.balance

    def _get_balance(self):
        return self.balance

    def process(self, operation_name, *args):
        if operation_name not in self.operations:
            raise ValueError(f"Operación no válida: {operation_name}")
        return self.operations[operation_name](*args)
