from Carro import Carro
from Aviao import Aviao

def mover_veiculo(veiculo):
    veiculo.mover()

# Chamando a função mover_veiculo() passando as instâncias das subclasses
mover_veiculo(Carro())
mover_veiculo(Aviao())
