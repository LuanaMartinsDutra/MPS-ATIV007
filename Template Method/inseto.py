# Manuela Cristina Pereira Bastos (2115310038)

from abc import ABC
class Insetos(ABC):
    def cicloDeVida(self):
        self.nascer()
        self.comer()
        self.reproduzir()
        self.morrer()

    def nascer(self):
        pass

    def comer(self):
        pass

    def reproduzir(self):
        pass

    def morrer(self):
        pass


class Mariposa(Insetos):
    def nascer(self):
        print("A mariposa está saindo do casulo")

    def comer(self):
        print("A mariposa está se alimentando")


class Besouro(Insetos):
    def comer(self):
        print("O besouro está se alimentando")

    def reproduzir(self):
        print("O besouro está se reproduzindo")

    def morrer(self):
        print("O besouro morreu")


def maePergunta(insetos: Insetos):
    insetos.cicloDeVida()

if __name__ == '__main__':
    print("A mariposa no jardim está fazendo o que?")
    maePergunta(Mariposa())
    print(" ")
    print("O besouro no jardim está fazendo o que?")
    maePergunta(Besouro())