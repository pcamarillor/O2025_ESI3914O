class BankAccount:
    def __init__(self, initial_balance = 0):
        # Validar que el saldo inicial no sea negativo
        if initial_balance < 0:
            raise ValueError("El saldo inicial no puede ser negativo")
        
        # Inicializar el saldo de la cuenta
        self.balance = float(initial_balance)
        
        # Crear diccionario de operaciones (mapeo de strings a funciones). Esto permite la ejecución dinámica de operaciones
        self.operations = {
            "deposit": self._deposit,
            "withdraw": self._withdraw,
            "get_balance": self._get_balance
        }
    
    def _deposit(self, amount):
        # Validar que la cantidad sea positiva
        if amount <= 0:
            raise ValueError("La cantidad a depositar debe ser mayor que cero")
        
        # Realizar el depósito
        old_balance = self.balance
        self.balance += amount

        return {
            "operation": "deposit",
            "amount": amount,
            "balance_before": old_balance,
            "balance_after": self.balance
        }
    
    def _withdraw(self, amount):
        # Validar que la cantidad sea positiva
        if amount <= 0:
            raise ValueError("La cantidad a retirar debe ser mayor que cero")
        
        # Validar que hay suficientes fondos
        if amount > self.balance:
            raise ValueError(f"Fondos insuficientes. Saldo actual: ${self.balance:.2f}")
        
        # Realizar el retiro
        old_balance = self.balance
        self.balance -= amount
        
        return {
            "operation": "withdraw",
            "amount": amount,
            "balance_before": old_balance,
            "balance_after": self.balance
        }
        
        return transaction
    
    def _get_balance(self):
        return {
            "operation": "get_balance",
            "current_balance": self.balance
        }
    
    def process(self, operation_name, *args, **kwargs):
        # Validar que la operación existe
        if operation_name not in self.operations:
            raise KeyError(f"Operación '{operation_name}' no disponible.")

        try:
            # Obtener la función correspondiente del diccionario
            operation_function = self.operations[operation_name]
            
            # Ejecutar la función dinámicamente con los argumentos proporcionados
            result = operation_function(*args, **kwargs)
            
            return result
            
        except Exception as exception:
            # Re-lanzar la excepción con información adicional
            raise Exception(f"Error al ejecutar operación '{operation_name}': {str(exception)}")

    def get_available_operations(self):
        return list(self.operations.keys())
    
    def __str__(self):
        return f"BankAccount(balance=${self.balance:.2f})"
    
    def __repr__(self):
        return f"BankAccount(balance={self.balance})"