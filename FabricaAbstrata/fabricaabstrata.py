from abc import ABC, abstractmethod

class AbstractFurnitureFactory(ABC):
    @abstractmethod
    def create_sofa(self):
        pass
    
    @abstractmethod
    def create_coffee_table(self):
        pass
    
    @abstractmethod
    def create_chair(self):
        pass

class VictorianFurnitureFactory(AbstractFurnitureFactory):
    def create_sofa(self):
        return VictorianSofa()
    
    def create_coffee_table(self):
        return VictorianCoffeeTable()
    
    def create_chair(self):
        return VictorianChair()

class ModernFurnitureFactory(AbstractFurnitureFactory):
    def create_sofa(self):
        return ModernSofa()
    
    def create_coffee_table(self):
        return ModernCoffeeTable()
    
    def create_chair(self):
        return ModernChair()

class AbstractSofa(ABC):
    @abstractmethod
    def sit_on(self):
        pass

class VictorianSofa(AbstractSofa):
    def sit_on(self):
        return "Você está sentado em um sofá vitoriano."

class ModernSofa(AbstractSofa):
    def sit_on(self):
        return "Você está sentado em um sofá moderno."

class AbstractCoffeeTable(ABC):
    @abstractmethod
    def put_on(self):
        pass

class VictorianCoffeeTable(AbstractCoffeeTable):
    def put_on(self):
        return f"Você coloca o livro em uma mesa de centro vitoriana."

class ModernCoffeeTable(AbstractCoffeeTable):
    def put_on(self):
        return f"Você coloca o livro em uma mesa de centro moderna."

class AbstractChair(ABC):
    @abstractmethod
    def sit_on(self):
        pass

class VictorianChair(AbstractChair):
    def sit_on(self):
        return "Você está sentado em uma cadeira vitoriana."

class ModernChair(AbstractChair):
    def sit_on(self):
        return "Você está sentado em uma cadeira moderna."

def client_code(factory: AbstractFurnitureFactory) -> None:
    sofa = factory.create_sofa()
    coffee_table = factory.create_coffee_table()
    chair = factory.create_chair()

    print(sofa.sit_on())
    print(coffee_table.put_on())
    print(chair.sit_on())

client_code(VictorianFurnitureFactory())
client_code(ModernFurnitureFactory())
