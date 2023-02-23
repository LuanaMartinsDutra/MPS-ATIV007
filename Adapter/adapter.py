""" 
A classe Old retorna o valor no tipo String 
"""
class Old:
    def get(self):
        return "Texto em String"

""" 
Já a classe New retorna o mesmo valor, porém utilizando-se de 
uma lista com valores de caracteres na tabela ASCII.
"""
class New:
    def get(self):
        return [84, 101, 120, 116, 111, 32, 101, 109, 32, 65, 83, 67, 73, 73]

"""
A classe Cliente recebe um objeto e printa o seu valor.
"""
class Cliente:
    def main(self, obj):
        print(obj.get())

"""
O padrão de projeto Adapter recomenda que não o cliente não
utilize o serviço diretamente, já que uma mudança neste acarretaria
a modificação total do código.

Mudando-se de classe, a função main teria que ser alterada
a cada vez para interpretar o novo tipo de dado, caso contrário
printaria apenas a lista com os valores em ASCII.
"""
# >>> if __name__ == '__main__':
# >>>     obj = Old()
# >>>     main(obj)
# [84, 101, 120, 116, 111, 32, 101, 109, 32, 65, 83, 67, 73, 73]

"""
O uso de uma classe auxiliar Adapter diminui drasticamente o 
acoplamento entre as classes de serviço e a classe Cliente. Assim, 
sempre que é necessário mudar o formato dos dados, apenas ela é 
modificada.
"""
class Adapter:

    def __init__(self, cls):
        self.cls = cls

    def get(self):
        res = ""
        for val in self.cls.get():
            res = res + chr(val)
        return res


"""
Desse modo, utiliza-se o adaptador a fim de que as classes não
se utilizem diretamente. Sempre que se utilizar um novo tipo de 
dados, modifica-se apenas o adaptador.
"""
if __name__ == '__main__':
    cli = Cliente()

    obj1 = Old()
    obj2 = Adapter(New())

    cli.main(obj1)
    cli.main(obj2)