class Object:
    def __init__(self, name, color):
        self.name = name
        self.color = color

class ObjectFlyweight:
    def __init__(self):
        self.objects = {}

    def get_object(self, name):
        if name not in self.objects:
            self.objects[name] = Object(name, None)
        return self.objects[name]


# Código de teste
object_flyweight = ObjectFlyweight()

object1 = object_flyweight.get_object('circle')
object1.color = 'green'

object2 = object_flyweight.get_object('square')
object2.color = 'blue'

object3 = object_flyweight.get_object('circle')
object3.color = 'red'

print("Objeto 1:", object1.name, object1.color)
print("Objeto 2:", object2.name, object2.color)
print("Objeto 3:", object3.name, object3.color)