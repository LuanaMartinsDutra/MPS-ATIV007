from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List


class Context():
    """
    O Contexto define a interface de interesse aos clientes.
    """

    def __init__(self, strategy: Strategy) -> None:
        """
        Normalmente, o Contexto aceita uma estratégia no construtor, mas 
        também fornece um setter para mudá-lo em tempo de execução.
        """

        self._strategy = strategy

    @property
    def strategy(self) -> Strategy:
        """
        O contexto mantém uma referência para um dos objetos de estrategia sem saber
        a classe concreta. Deverá trabalhar com todas através da interface Strategy.
        """

        return self._strategy

    @strategy.setter
    def strategy(self, strategy: Strategy) -> None:
        """
        Normalmente, o contexto permite alterar o objeto Strategy em tempo de execução.
        """

        self._strategy = strategy

    def do_some_business_logic(self) -> None:
        """
        O contexto realiza o trabalho o enviando para o objeto Strategy em vez de implementar
        variações do algoritmo em si.
        """

        # ...

        print("Contexto: Realizando a operação matemática (não sei qual)")
        result = self._strategy.do_algorithm((1, 2))
        print(result)

        # ...


class Strategy(ABC):
    """
    Esta interface declara operações comuns a todas variações do mesmo algoritmo.
    O contexto usa esta interface para chamar o algoritmo definido nas Contrete
    Strategies/Estratégias Concretas.
    """

    @abstractmethod
    def do_algorithm(self, data: List):
        pass


"""
Contrete Strategies/Estratégias Concretas implementam o algoritmo seguindo a 
interface, tornando substituíveis. 
"""


class ConcreteStrategyA(Strategy):
    def do_algorithm(self, data: List) -> int:
        return sum(data)


class ConcreteStrategyB(Strategy):
    def do_algorithm(self, data: List) -> int:
        x =1 
        for i in data:
            x = x * i 
        return x


if __name__ == "__main__":
    # O código do cliente seleciona uma estratégia e envia para o contexto.
    context = Context(ConcreteStrategyA())
    print("Cliente: Strategy está como operação de soma")
    context.do_some_business_logic()
    print()

    print("Cliente: Strategy está como operação de multiplicação")
    context.strategy = ConcreteStrategyB()
    context.do_some_business_logic()