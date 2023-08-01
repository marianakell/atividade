from Forma import Forma

class Circulo(Forma):
    def __init__(self, raio):
        super().__init__("Círculo", "Forma redonda")
        self.raio = raio

    def calcular_area(self):
        return 3.14159 * self.raio ** 2

    def calcular_perimetro(self):
        return 2 * 3.14159 * self.raio
