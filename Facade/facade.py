# Lista de subsistemas
class DecoratedText:
    def __init__(self):
        self.decoration = {}
        self.decoration[1] = '\033[0m'   # ENDC
        self.decoration[2] = '\033[1m'   # BOLD
        self.decoration[3] = '\033[4m'   # UNDERLINE
        self.decoration[4] = '\033[91m'  # FAIL
        self.decoration[5] = '\033[92m'  # OKGREEN
        self.decoration[6] = '\033[93m'  # WARNING
        self.decoration[7] = '\033[94m'  # OKBLUE
        self.decoration[8] = '\033[95m'  # HEADER
        self.decoration[9] = '\033[96m'  # OKCYAN
    
    def print_decorated_text(self, text, keydecoration):
        print(f"{self.decoration[keydecoration]}{text}{self.decoration[1]}")

class ToDoList:
    def __init__(self):
        self.list = []
    
    def add_task(self, task):
        # 0 - Active
        # 1 - Done
        # 2 - Canceled
        self.list.append([len(self.list), task, 0])
    
    def remove_task(self, id):
        self.list.pop(id)
    
    def change_task_status(self, id, status):
        self.list[id][2] = status
    
    def get_list(self):
        return self.list
    
    def display_list(self):
        for task in self.list:
            print("- " + task[1])









            

# Facade
class Facade:
    def __init__(self):
        self.deco = DecoratedText()
        self.todo = ToDoList()
    
    def add_task(self, task):
        self.todo.add_task(task)
    
    def remove_task(self, id):
        self.todo.remove_task(id)
    
    def change_task_status(self, id, status):
        self.todo.change_task_status(id, status)
    
    def display_list(self):
        aux = self.todo.get_list()
        self.deco.print_decorated_text("\n---------- Taks ----------\n", 2)
        for task in aux:
            match task[2]:
                case 0:
                    print(str(task[0]) + " - " + task[1])
                case 1:
                    self.deco.print_decorated_text(
                        str(task[0]) + " - " + task[1],
                        5
                    )
                case 2:
                    self.deco.print_decorated_text(
                        str(task[0]) + " - " + task[1],
                        4
                    )
    
    def display_active_tasks(self):
        aux = self.todo.get_list()
        self.deco.print_decorated_text("\n---------- Active Taks ----------\n", 2)
        for task in aux:
            if task[2] == 0:
                print(str(task[0]) + " - " + task[1])
    
    def display_done_tasks(self):
        aux = self.todo.get_list()
        self.deco.print_decorated_text("\n---------- Done Taks ----------\n", 2)
        for task in aux:
            if task[2] == 1:
                self.deco.print_decorated_text(str(task[0]) + " - " + task[1], 5)
    
    def display_canceled_tasks(self):
        aux = self.todo.get_list()
        self.deco.print_decorated_text("\n---------- Canceled Taks ----------\n", 2)
        for task in aux:
            if task[2] == 2:
                self.deco.print_decorated_text(str(task[0]) + " - " + task[1], 4)












## Aplicação com o Facade
facade = Facade()
facade.add_task("Fazer a tarefa de MPS")
facade.add_task("Varrer o quarto")
facade.add_task("Tirar o lixo")
facade.add_task("Comprar pão")
facade.add_task("Levar o cachorro pra passear")
facade.add_task("Ir ao oftalmologista")
facade.add_task("Visitar a irmã Maria")
facade.add_task("Lavar a louça")
facade.add_task("Trabalho de empreendedorismo")
facade.add_task("Pagar a fatura do cartão")
facade.add_task("Aniversãrio do papai")
facade.add_task("Trocar a senha do wi-fi")
facade.change_task_status(1, 1)
facade.change_task_status(3, 1)
facade.change_task_status(6, 1)
facade.change_task_status(5, 2)
facade.change_task_status(8, 2)
facade.change_task_status(9, 2)

facade.display_list()
facade.display_active_tasks()
facade.display_done_tasks()
facade.display_canceled_tasks()