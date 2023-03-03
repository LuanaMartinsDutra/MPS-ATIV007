
# IMPLEMENTAÇÃO DO PADRÃO OBSERVER


# Classe base abstrata Observer
class Observer:
    # Com um metodo de atualização que todos os observers devem implementar
    def update(self, message):
        pass

# Classe Subject que mantém uma lista de observadores e fornece varios métodos


class Subject:
    def __init__(self):
        self.observers = []

    def attach(self, observer):
        self.observers.append(observer)

    def detach(self, observer):
        self.observers.remove(observer)

    def notify_observers(self, message):
        for observer in self.observers:
            observer.update(message)

# A Classe ConcreteObserver ela recebe atualizações do Subject e imprime a mensagem no console


class ConcreteObserver(Observer):
    def __init__(self, name):
        self.name = name

    def update(self, message):
        print(f"{self.name} received message: {message}")


# Na main criamos um Subject e dois ConcreteObs
def main():
    subject = Subject()
    observer1 = ConcreteObserver("Observer 1")
    observer2 = ConcreteObserver("Observer 2")

# Anexa ambos observadores
    subject.attach(observer1)
    subject.attach(observer2)

# Notifica sobre uma mensagem
    subject.notify_observers("Hello, observers!")

# Desanexa um dos observadores
    subject.detach(observer2)

# Os notifica novamente
    subject.notify_observers("Goodbye, observer 2!")


# A saída deve mostrar que ambos os observadores recebema primeira mensagem

# Mas somente o primeiro Obs recebe a segunda mensagem depois que o segundo é desanexado
if __name__ == "__main__":
    main()
