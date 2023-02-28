from abc import ABC, abstractmethod

class Inseto(ABC):

    @abstractmethod
    def nascer(self):
        pass

    @abstractmethod
    def crescer(self):
        pass

    @abstractmethod
    def reproduzir(self):
        pass

    @abstractmethod
    def morrer(self):
        pass

    def cicloDeVida(self):
        self.nascer()
        self.crescer()
        self.reproduzir()
        self.morrer()

class Lesma(Inseto):

    def nascer(self):
        print("A lesma nasceu")

    def crescer(self):
        print("A lesma está comendo")

    def reproduzir(self):
        print("A lesma está se reproduzindo")

    def morrer(self):
        print("A lesma morreu")

class Besouro(Inseto):

    def nascer(self):
        print("O besouro nasceu")

    def crescer(self):
        print("O besouro está coletando néctar")

    def morrer(self):
        print("O besouro morreu")

lesma = Lesma()

besouro = Besouro()

print("Ciclo de vida da formiga:")
lesma.cicloDeVida()

print("Ciclo de vida da abelha:")
besouro.cicloDeVida()