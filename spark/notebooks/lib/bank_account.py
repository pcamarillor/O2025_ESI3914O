class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance
        
        #Diccionario para hacer las operaciones 
        self.operations = {
            "deposit": self.deposit,
            "withdraw": self.withdraw,
            "get_balance": self.get_balance
        }

    #Definimos deposito
    def deposit(self, amount):
        #Tiene que ser mayor a 0 la cantidad de dinero 
        if amount > 0:
            #Se agrega lo depositado al balance de la cuenta
            self.balance += amount
            return f"Depositado {amount}. Nuevo Balance: {self.balance}"
        return "Cantidad invalida de dinero."

    #Definimos retiro
    def withdraw(self, amount):
        #Mayor a cero y menor o igual al balance actual
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            return f"Retiraste {amount}. Nuevo Balance: {self.balance}"
        return "Fondos Insuficientes"
        
    #Muestra el balance actual
    def get_balance(self):
        return f"Balance Actual: {self.balance}"

    #Clausula en caso de que se quiera hacer una operacion que no existe 
    def process(self, operation, *args):
        if operation in self.operations:
            return self.operations[operation](*args)
        else:
            return f"La Operacion '{operation}' no existe."