from ContaBancaria import ContaBancaria
from ContaCorrente import ContaCorrente
from ContaPoupanca import ContaPoupanca

# Criando instâncias das classes
conta_bancaria = ContaBancaria("1234", 1000)
conta_corrente = ContaCorrente("5678", 2000, 500)
conta_poupanca = ContaPoupanca("9101", 3000, 0.05)

# Utilizando os métodos depositar e sacar
conta_bancaria.depositar(500)
conta_bancaria.sacar(200)
conta_corrente.depositar(1000)
conta_corrente.sacar(300)
conta_poupanca.depositar(2000)
conta_poupanca.sacar(500)

# Chamando o método detalhesConta
conta_bancaria.detalhesConta()
print("\n")
conta_corrente.detalhesConta()
print("\n")
conta_poupanca.detalhesConta()
