from Animal import Animal
from Cachorro import Cachorro
from Gato import Gato

def emitir_som(animal):
    animal.emitir_som()

# Chama o método emitir_som() da classe Animal
emitir_som(Animal())
# Chama o método emitir_som() da classe Cachorro
emitir_som(Cachorro())
# Chama o método emitir_som() da classe Gato
emitir_som(Gato())
