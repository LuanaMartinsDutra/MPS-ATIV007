# Feito por Arthur Uguen de Mendonça

""" 
A classe FornecedorString retorna o valor no tipo String 
"""
class FornecedorString:

    def __init__(self, nome):
        self.__nome = nome

    def get(self):
        return "Texto em String"

""" 
Já a classe FornecedorASCII retorna o mesmo valor, porém utilizando-se de 
uma lista com valores de caracteres na tabela ASCII.
"""
class FornecedorAscii:

    def __init__(self, nome):
        self.__nome = nome

    def get(self):
        return [84, 101, 120, 116, 111, 32, 101, 109, 32, 65, 83, 67, 73, 73]

"""
A classe Cliente recebe um objeto e printa o seu valor.
"""
class Cliente:

    def __init__(self, nome):
        self.__nome = nome

    def exibe_valor_recebido(self, obj):
        return obj.get()

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

class AdapterInterface:
    def get() -> str:
        pass
    
class AdapterAscii(AdapterInterface):

    def __init__(self, adaptee):
        self.__adaptee = adaptee

    def get(self):
        res = ""
        for val in self.__adaptee.get():
            res = res + chr(val)
        return res

class AdapterString(AdapterInterface):

    def __init__(self, adaptee):
        self.__adaptee = adaptee

    def get(self):
        return self.__adaptee.get()

"""
Desse modo, utiliza-se o adaptador a fim de que as classes não
se utilizem diretamente. Sempre que se utilizar um novo tipo de 
dados, modifica-se apenas o adaptador.
"""
if __name__ == '__main__':
    cli = Cliente("Fulano")
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    print("\033[32mVersão Arcaica: \033[00m")
    obj0 = FornecedorString("Stringly")
    print(f"Valor recebido: \033[93m{cli.exibe_valor_recebido(obj0)}\033[00m")
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    print("\033[32mVersão com Adapter: \033[00m")
    obj1 = AdapterString(FornecedorString(nome="Stringly"))
    obj2 = AdapterAscii(FornecedorAscii(nome="Asciily"))
    print(f"Valor recebido pelo cliente: \033[93m{cli.exibe_valor_recebido(obj1)}\033[00m")
    print(f"Valor recebido pelo cliente: \033[93m{cli.exibe_valor_recebido(obj2)}\033[00m")
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")