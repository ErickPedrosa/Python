
class Conta:
    def __init__(self, numero, titular, saldo, limite):
        print(f"Construindo o objeto ... {self}")
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        self.__codigo_banco = "001"
        
    def extrato(self):
        print(f"Saldo de {self.__saldo} do titular {self.__titular}")

    def depositar(self, valor):
        self.__saldo += valor
        
    def __pode_sacar(self, valor_a_sacar):
        valor_disponivel = self.__saldo + self.__limite
        return (valor_a_sacar <= valor_disponivel)

    def sacar(self, valor):
        if (self.__pode_sacar()):
            self.__saldo -= valor
        else:
            print(f"O valor {valor} passou do limite")
        
    def transferir(self, destino, valor):
        self.sacar(valor)
        destino.depositar(valor)
      
    @property  
    def saldo(self):
        return self.__saldo
        
    @property
    def titular(self):
        return self.__titular
        
    @property
    def limite(self):
        return self.__limite
        
    @limite.setter
    def set_limite(self, limite):
        self.__limite = limite
    
    @staticmethod
    def codigo_banco():
        return "001"
    
    @staticmethod
    def codigos_bancos():
        return {"BB":"001", "Caixa":"104", "Bradesco":"237"}
    
        