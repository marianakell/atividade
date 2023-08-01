from Circulo import Circulo
from Retangulo import Retangulo

# Criando objetos e obtendo os resultados dos cálculos
circulo = Circulo(5)
retangulo = Retangulo(4, 6)

area_circulo = circulo.calcular_area()
perimetro_circulo = circulo.calcular_perimetro()

area_retangulo = retangulo.calcular_area()
perimetro_retangulo = retangulo.calcular_perimetro()

print("Círculo:")
print(circulo.dados_da_forma())
print("Área:", area_circulo)
print("Perímetro:", perimetro_circulo)

print("\nRetângulo:")
print(retangulo.dados_da_forma())
print("Área:", area_retangulo)
print("Perímetro:", perimetro_retangulo)
