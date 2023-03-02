class Object:
    def __init__(self, name, color):
        self.name = name
        self.color = color

class NameFlyweight:
    def __init__(self):
        self.names = {}

    def get_name(self, name):
        if name not in self.names:
            self.names[name] = name
        return self.names[name]

class ColorFlyweight:
    def __init__(self):
        self.colors = {}

    def get_color(self, color):
        if color not in self.colors:
            self.colors[color] = color
        return self.colors[color]

class ObjectFlyweight:
    def __init__(self):
        self.names = NameFlyweight()
        self.colors = ColorFlyweight()
        self.objects = {}

    def get_object(self, name, color):
        name = self.names.get_name(name)
        color = self.colors.get_color(color)
        if (name, color) not in self.objects:
            self.objects[(name, color)] = Object(name, color)
        return self.objects[(name, color)]


# Código de teste
object_flyweight = ObjectFlyweight()

object1 = object_flyweight.get_object('circle', 'green')
object2 = object_flyweight.get_object('square', 'blue')
object3 = object_flyweight.get_object('circle', 'red')
object4 = object_flyweight.get_object('triangle', 'red')

print("Objeto 1:", object1.name, object1.color)
print("Objeto 2:", object2.name, object2.color)
print("Objeto 3:", object3.name, object3.color)
print("Objeto 4:", object4.name, object4.color)