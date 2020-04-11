class Conta:

    def __init__(self, numero, titular, saldo, limite):
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        self.__cod_banco = "777"

    def deposito(self, valor):
        self.__saldo += valor

    def __aprov_saque(self, valor_saque):
        valor_disponivel = self.__saldo + self.__limite
        return valor_saque <= valor_disponivel

    def saque(self, valor):
        if(self.__aprov_saque(valor)):
            self.__saldo -= valor
        else:
            print('Saldo insuficiente.')

    def extrato(self):
        print(f'{self.__titular}, o saldo disponível é de R$ {self.__saldo:.2f}.')

    def transfere(self, valor,  destino):
        self.saque(valor)
        destino.deposito(valor)

    def get_saldo(self):
        return self.__saldo

    def get_titular(self):
        return self.__titular
    @property
    def limite(self):
        return self.__limite
    @limite.setter
    def limite(self, limite):
        self.__limite = limite

    @staticmethod
    def cod_banco():
        return __cod_banco