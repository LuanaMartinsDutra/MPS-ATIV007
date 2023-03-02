from InterfaceCommand import CommandInterface
import TV
class  ControleRemoto(CommandInterface):
    tv = TV
    def __init__(self, tv):
        self.tv = tv

    def execute(self):
        self.tv.ligar()

    def undo(self):
        self.tv.desligar()
