from abc import ABC, abstractmethod


class Creator(ABC):
    """
    A classe Creator declara o método fábrica que deve retornar 
    um objeto de uma classe Product. As subclasses do Creator 
    geralmente fornecem a implementação desse método.
    """

    @abstractmethod
    def factory_method(self):
        """
        Observe que o Criador também pode fornecer alguma 
        implementação padrão do método de fábrica.
        """
        pass

    def some_operation(self) -> str:
        """
        Observe também que, apesar do nome, a responsabilidade primária
        do Criador não é criar produtos. Normalmente, ele contém alguma 
        lógica de negócios central que depende de objetos Product, retornados 
        pelo método de fábrica. As subclasses podem alterar indiretamente essa
        lógica de negócios substituindo o método de fábrica e retornando um tipo
        diferente de produto a partir dele.
        """

        # Chama o factory method para criar um objeto Product.
        product = self.factory_method()

        # Usa o product
        result = f"Criador: o código do mesmo criador acabou de funcionar com {product.operation()}"

        return result


"""
Os Concrete Creators substituem (override) o factory method para alterar 
o tipo do produto resultante.
"""

class Product(ABC):
    """
    A interface Product declara as operações que todos os Concrete Products
    devem implementar.
    """

    @abstractmethod
    def operation(self) -> str:
        pass


class ConcreteCreator1(Creator):
    """
    Observe que a assinatura do método ainda usa o tipo de produto abstrato, mesmo 
    que o produto concreto seja realmente retornado do método. Desta forma, o Criador 
    pode ficar independente de classes de produtos concretos.
    """

    def factory_method(self) -> Product:
        return ConcreteProduct1()


class ConcreteCreator2(Creator):
    def factory_method(self) -> Product:
        return ConcreteProduct2()

"""
Concrete Products fornecem várias implementações da interface Product.
"""

class ConcreteProduct1(Product):
    def operation(self) -> str:
        return "{Resultado do ConcreteProduct1}"


class ConcreteProduct2(Product):
    def operation(self) -> str:
        return "{Resultado ConcreteProduct2}"


def client_code(creator: Creator) -> None:
    """
    O código do cliente funciona com uma instância de um oncrete creator, embora 
    por meio de sua interface básica. Desde que o cliente continue trabalhando com
    o creator por meio da interface base, você pode passar para ele qualquer subclasse do creator.
    """

    print(f"Cliente: Não conhece a classe Creator, mas ainda funciona...\n"
          f"{creator.some_operation()}", end="")


if __name__ == "__main__":
    print("App: Launched com o ConcreteCreator1.")
    client_code(ConcreteCreator1())
    print("\n")

    print("App: Launched com o ConcreteCreator2.")
    client_code(ConcreteCreator2())