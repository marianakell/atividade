from Forma import Forma

class Retangulo(Forma):
    def __init__(self, lado1, lado2):
        super().__init__("Retângulo", "Forma com lados perpendiculares")
        self.lado1 = lado1
        self.lado2 = lado2

    def calcular_area(self):
        return self.lado1 * self.lado2

    def calcular_perimetro(self):
        return 2 * (self.lado1 + self.lado2)
