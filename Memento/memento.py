class Memento:
    # Classe Memento contém o estado do objeto a ser restaurado.
    def __init__(self, state):
        self._state = state
        
    def get_state(self):
        return self._state
