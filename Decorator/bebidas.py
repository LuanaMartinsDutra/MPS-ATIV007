# Debora Souza Barros

from abc import ABC, abstractmethod


# interface do componente
class Bebida(ABC):

    def __init__(self):
        self.descricao = ""


    def get_descricao(self):
        return self.descricao


    def get_preco(self):
        pass


# componente concreto
class Expresso(Bebida):

    def __init__(self):
        super().__init__()
        self.descricao = "Café Expresso"


    def get_preco(self):
        return 1.50


# decorator
class DecoratorBebida(Bebida):

    def __init__(self, bebida):
        super().__init__()
        self.bebida = bebida


    def get_descricao(self):
        pass


# decorator concreto
class Caramelo(DecoratorBebida):

    def __init__(self, bebida):
        super().__init__(bebida)


    def get_descricao(self):
        return self.bebida.get_descricao() + ", Caramelo"


    def get_preco(self):
        return self.bebida.get_preco() + 0.85


# decorator concreto
class Chocolate(DecoratorBebida):

    def __init__(self, bebida):
        super().__init__(bebida)


    def get_descricao(self):
        return self.bebida.get_descricao() + ", Chocolate"


    def get_preco(self):
        return self.bebida.get_preco() + 1.00


if __name__ == "__main__":

    expresso = Expresso()
    print(expresso.get_descricao() + " | R$ " + str(expresso.get_preco()))

    Chocolate = Chocolate(expresso)
    print(Chocolate.get_descricao() + " | R$ " + str(Chocolate.get_preco()))

    caramelo = Caramelo(Chocolate)
    print(caramelo.get_descricao() + " | R$ " + str(caramelo.get_preco()))
