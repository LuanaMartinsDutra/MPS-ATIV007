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