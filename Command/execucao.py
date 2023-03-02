import TV
import ControleRemoto

tv = TV
controle = ControleRemoto.ControleRemoto(tv)
controle.execute()
controle.undo()
