import copy
# Larry Amaral Reis - 2115310067
#          +--------------+
#          | Stormtrooper |
#          +--------------+
#          | - name       |
#          | - age        |
#          | - designation|
#          +--------------+
#          | + clone()    |
#          +--------------+
#                  ^
#                  |      
#                  |     
#      +------------------------+ 
#      |   tk_421_prototype     |
#      +------------------------+ 
#      |- name: "TK-421"        | 
#      |- age: 29               |
#      |- designation: "Trooper"|
#      +------------------------+
#      |+ clone()               | 
#      +------------------------+  
#                  ^
#                  |
#      +------------------------+ 
#      |          tk_421        |
#      +------------------------+ 
#      |- name: "TK-421"        | 
#      |- age: 29               |
#      |- designation: "Trooper"|
#      +------------------------+
#      |+ clone()               | 
#      +------------------------+  

class Stormtrooper:
    def __init__(self, name, age, designation):
        self.name = name
        self.age = age
        self.designation = designation

    def clone(self):
        return copy.deepcopy(self)


# Criando um protótipo de Stormtrooper
tk_421_prototype = Stormtrooper("TK-421", 29, "Trooper")

# Clonando o protótipo para criar um novo Stormtrooper
tk_421 = tk_421_prototype.clone()

# Modificando a propriedade do novo Stormtrooper
#tk_421.designation = "Squad Leader"

# Imprimindo as informações dos Stormtroopers
print(tk_421_prototype.name, tk_421_prototype.age, tk_421_prototype.designation)
print(tk_421.name, tk_421.age, tk_421.designation)
