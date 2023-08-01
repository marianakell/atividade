class Forma:
    def __init__(self, tipo, descricao):
        self.tipo = tipo
        self.descricao = descricao

    def dados_da_forma(self):
        return f"Tipo: {self.tipo}\nDescrição: {self.descricao}"

    def calcular_area(self):
        return "Não há dados suficientes para realizar o cálculo."

    def calcular_perimetro(self):
        return "Não há dados suficientes para realizar o cálculo."
