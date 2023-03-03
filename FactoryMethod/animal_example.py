from abc import ABC, abstractmethod

# Classe abstrata que define a interface comum para todos os animais que podem ser criados
class Animal():
    @abstractmethod
    def make_sound(self):
        pass

# Classes que implementam a interface Animal
class Dog(Animal):
    def make_sound(self):
        return "au au"

class Cat(Animal):
    def make_sound(self):
        return "miau"

# Classe abstrata que contém um factory method abstrato para criar objetos Animal
class AnimalFactory():
    @abstractmethod
    def create_animal(self) -> Animal:
        pass

# Classes que estendem a AnimalFactory, cada uma responsável por criar um tipo específico de animal
class DogFactory(AnimalFactory):
    def create_animal(self) -> Animal:
        return Dog()

class CatFactory(AnimalFactory):
    def create_animal(self) -> Animal:
        return Cat()

# Cliente que usa a AnimalFactory para criar diferentes tipos de animais
class AnimalClient:
    def __init__(self, factory: AnimalFactory):
        self.factory = factory

    def get_animal_sound(self):
        animal = self.factory.create_animal()
        return animal.make_sound()

if __name__ == "__main__":
    dog_factory = DogFactory()
    client = AnimalClient(dog_factory)
    print(client.get_animal_sound())

    cat_factory = CatFactory()
    client = AnimalClient(cat_factory)
    print(client.get_animal_sound())
