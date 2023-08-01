from ContaBancaria import ContaBancaria

class ContaPoupanca(ContaBancaria):
    def __init__(self, numeroConta, saldo, taxaRendimento):
        super().__init__(numeroConta, saldo)
        self.taxaRendimento = taxaRendimento

    def detalhesConta(self):
        super().detalhesConta()
        print("Taxa de rendimento:", self.taxaRendimento)
