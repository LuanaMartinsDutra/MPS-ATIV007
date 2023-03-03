# VIsitor

# ALexandre Bruno Mota dos Santos

# Importa Das Blibiotecas
from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List

class Component(ABC):
    """
    A interface Component declara um método accept que deve receber
    como argumento a interface base do visitante.
    """

    @abstractmethod
    def accept(self, visitor: Visitor) -> None:
        pass


class ConcreteComponentA(Component):
    """
    Cada componente concreto deve implementar o método accept de tal forma que
    ele chama o método do visitante correspondente à classe do componente.
    """

    def accept(self, visitor: Visitor) -> None:
        """
        Note que estamos chamando visitConcreteComponentA, que corresponde ao nome da
        classe atual. Dessa forma, informamos ao visitante a classe do componente com
        o qual ele está trabalhando.
        """

        visitor.visit_concrete_component_a(self)

    def exclusive_method_of_concrete_component_a(self) -> str:
        """
        Componentes concretos podem ter métodos especiais que não existem em sua classe
        ou interface base. O visitante ainda é capaz de usar esses métodos, uma vez que
        ele está ciente da classe concreta do componente.
        """

        return "A"


class ConcreteComponentB(Component):
    """
    Igual aqui: visitConcreteComponentB => ConcreteComponentB
    """

    def accept(self, visitor: Visitor):
        visitor.visit_concrete_component_b(self)

    def special_method_of_concrete_component_b(self) -> str:
        return "B"


class Visitor(ABC):
    """
    A interface Visitor declara um conjunto de métodos de visitação que correspondem às classes
    de componentes. A assinatura de um método de visitação permite que o visitante identifique a
    classe exata do componente com o qual está lidando.
    """

    @abstractmethod
    def visit_concrete_component_a(self, element: ConcreteComponentA) -> None:
        pass

    @abstractmethod
    def visit_concrete_component_b(self, element: ConcreteComponentB) -> None:
        pass


"""
Visitantes concretos implementam várias versões do mesmo algoritmo, que podem trabalhar com todas
as classes concretas de componentes.

Você pode experimentar o maior benefício do padrão Visitor ao usá-lo com uma estrutura de objeto complexa,
como uma árvore de Composite. Nesse caso, pode ser útil armazenar algum estado intermediário do algoritmo
enquanto executa os métodos do visitante em vários objetos da estrutura.
"""


class ConcreteVisitor1(Visitor):
    def visit_concrete_component_a(self, element) -> None:
        print(f"{element.exclusive_method_of_concrete_component_a()} + ConcreteVisitor1")

    def visit_concrete_component_b(self, element) -> None:
        print(f"{element.special_method_of_concrete_component_b()} + ConcreteVisitor1")


class ConcreteVisitor2(Visitor):
    def visit_concrete_component_a(self, element) -> None:
        print(f"{element.exclusive_method_of_concrete_component_a()} + ConcreteVisitor2")

    def visit_concrete_component_b(self, element) -> None:
        print(f"{element.special_method_of_concrete_component_b()} + ConcreteVisitor2")


def client_code(components: List[Component], visitor: Visitor) -> None:
    """
    O código do cliente pode executar operações de visitante em qualquer conjunto de elementos sem precisar
    descobrir suas classes concretas. A operação accept direciona uma chamada para a operação apropriada no
    objeto visitante.
    """

    # ...
    for component in components:
        component.accept(visitor)
    # ...


if __name__ == "__main__":
    components = [ConcreteComponentA(), ConcreteComponentB()]

    print("O código do cliente funciona com todos os visitantes por meio da interface básica do visitante:")
    visitor1 = ConcreteVisitor1()
    client_code(components, visitor1)

    print("Permite que o mesmo código de cliente funcione com diferentes tipos de visitantes:")
    visitor2 = ConcreteVisitor2()
    client_code(components, visitor2)