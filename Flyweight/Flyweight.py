class Object:
    def __init__(self, name, color):
        self.name = name
        self.color = color

class ObjectFlyweight:
    def __init__(self):
        self.name_objects = {}
        self.color_objects = {}

    def get_object(self, name, color):
        # Verifica se já existe um objeto com o mesmo nome na lista de objetos de nome
        if name not in self.name_objects:
            # Se não existir, cria um novo objeto e adiciona na lista de objetos de nome
            self.name_objects[name] = Object(name, None)
        # Verifica se já existe um objeto com a mesma cor na lista de objetos de cor
        if color not in self.color_objects:
            # Se não existir, cria um novo objeto e adiciona na lista de objetos de cor
            self.color_objects[color] = Object(None, color)
        # Retorna um novo objeto com o mesmo nome e cor dos objetos existentes na lista
        return Object(name, color)

# Cria uma nova instância da classe ObjectFlyweight
object_flyweight = ObjectFlyweight()

# Utiliza o padrão flyweight para criar objetos
object1 = object_flyweight.get_object('circle', 'green')
object2 = object_flyweight.get_object('square', 'blue')
object3 = object_flyweight.get_object('circle', 'green')

# Imprime as informações dos objetos criados
print("Objeto 1:", object1.name, object1.color)
print("Objeto 2:", object2.name, object2.color)
print("Objeto 3:", object3.name, object3.color)