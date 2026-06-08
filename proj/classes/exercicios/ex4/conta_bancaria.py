class ContaBancaria:
    titular: str
    saldo: float = 0.0

    def __init__(self, titular:str):
        self.titular = titular
    
    def depositar(self, valor: float):
        if valor > 0:
            self.saldo = self.saldo + valor
    
    def sacar(self, valor: float) -> bool:
        if self.saldo - valor < 0:
            return False
        
        self.saldo = self.saldo - valor
        return True