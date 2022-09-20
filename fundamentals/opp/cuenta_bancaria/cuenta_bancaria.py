class CuentaBancaria:
    nombre_banco = "Primer Dojo Nacional"
    todas_las_cuentas = []

    def __init__(self, tasa_interes, balance):
        self.tasa_interes = tasa_interes
        self.balance = balance
        CuentaBancaria.todas_las_cuentas.append(self)

    def re_tiro(self,cantidad):
        if CuentaBancaria.puede_retirar(self.balance,cantidad):
            self.balance -= cantidad
        else:
            print("Fondos insuficientes")
        return self 

    def deposito(self, cantidad):
        self.balance += cantidad
        return self


    def retiro(self, cantidad):
        if self.balance < cantidad:
            self.balance -= 5
            print("Fondos Insuficientes, te restaremos 5")
        else:
            self.balance -= cantidad
        return self

    def mostrar_info_cuenta(self):
        print("Balance actual: ", self.balance)
        return self


    def generar_interes(self):
        if self.balance > 0:
            self.balance = self.balance + (self.balance * self.tasa_interes)  
        return self

    @classmethod
    def cambiar_nombre_banco(cls, name):
        cls.nombre_banco = name

    
    @classmethod
    def todos_los_balances(cls):
       
        for account in cls.todas_las_cuentas:
            sum += balance.cuenta
        return sum

    @classmethod
    def imprimir_todas_cuentas(cls):
        for cuenta in cls.todas_las_cuentas:
            print(f"Esta cuenta tiene un balance de {cuenta.balance}")
           
    @staticmethod
    def puede_retirar(balance,cantidad):
        if (balance - cantidad) < 0:
            return False
        else:
            return True
