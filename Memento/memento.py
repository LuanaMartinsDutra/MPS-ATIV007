class Memento:
    # Classe Memento contém o estado do objeto a ser restaurado.
    def __init__(self, state):
        self._state = state
        
    def get_state(self):
        return self._state

class Originator:
    """
    Classe Originator cria um Memento contendo um snapshot do seu estado atual e
    utiliza um Memento para restaurar o seu estado anterior.
    """
    def __init__(self, state):
        self._state = state
    
    def set_state(self, state):
        print(f"Originator: Mudando estado para {state}")
        self._state = state
    
    def save_state(self):
        print("Originator: Salvando estado em Memento")
        return Memento(self._state)
    
    def restore_state(self, memento):
        self._state = memento.get_state()
        print(f"Originator: Estado restaurado para {self._state}")


class Caretaker:
    """
    Classe Caretaker é responsável por armazenar os Mementos e garantir que não sejam alterados.
    """
    def __init__(self, originator):
        self._mementos = []
        self._originator = originator
        
    def backup(self):
        print("Caretaker: Fazendo backup do estado do Originator...")
        self._mementos.append(self._originator.save_state())
        
    def undo(self):
        if not self._mementos:
            return
        
        memento = self._mementos.pop()
        print(f"Caretaker: Restaurando estado para {memento.get_state()}")
        self._originator.restore_state(memento)

# Exemplo de uso:
if __name__ == "__main__":
    # Cria o Originator e o Caretaker
    originator = Originator("Estado Inicial")
    caretaker = Caretaker(originator)
    
    # Faz mudanças no estado do Originator e faz backups
    caretaker.backup()
    originator.set_state("Estado 1")
    caretaker.backup()
    originator.set_state("Estado 2")
    caretaker.backup()
    originator.set_state("Estado 3")
    
    # Restaura o estado anterior usando o Caretaker
    caretaker.undo()
    caretaker.undo()
    caretaker.undo()