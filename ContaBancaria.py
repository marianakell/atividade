class ContaBancaria:
    def __init__(self, numeroConta, saldo):
        self.numeroConta = numeroConta
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
        else:
            print("Saldo insuficiente.")

    def detalhesConta(self):
        print("Número da conta:", self.numeroConta)
        print("Saldo:", self.saldo)
