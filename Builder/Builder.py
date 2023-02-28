class Carro:
    def __init__(self, marca="", modelo="", cor="", ano=0, motor="", combustivel=""):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.ano = ano
        self.motor = motor
        self.combustivel = combustivel

    def __str__(self):
        return f"{self.marca} {self.modelo} ({self.cor}, {self.ano}) - Motor: {self.motor}, Combustível: {self.combustivel}"


class CarroBuilder:
    def __init__(self, marca="", modelo="", cor="", ano=0, motor="", combustivel=""):
        self.carro = Carro(marca, modelo, cor, ano, motor, combustivel)

    def set_marca(self, marca):
        self.carro.marca = marca
        return self

    def set_modelo(self, modelo):
        self.carro.modelo = modelo
        return self

    def set_cor(self, cor):
        self.carro.cor = cor
        return self

    def set_ano(self, ano):
        self.carro.ano = ano
        return self

    def set_motor(self, motor):
        self.carro.motor = motor
        return self

    def set_combustivel(self, combustivel):
        self.carro.combustivel = combustivel
        return self

    def build(self):
        return self.carro
        
builder = CarroBuilder()
carro = builder.set_marca("Ford").set_modelo("Fiesta").set_cor("Prata").set_ano(2021).set_motor("1.6L").set_combustivel("Gasolina").build()

print(carro)
