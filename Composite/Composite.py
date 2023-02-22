class Employee:

    def __init__(self, *args):
        self.position = args[0]

    def show_details(self):
        print("\t", end="")
        print(self.position)


class Management:

    def __init__(self, *args):
        self.position = args[0]
        self.children = []

    def add(self, child):
     self.children.append(child)

    def remove(self, child):
        self.children.remove(child)

    def show_details(self):
        print(self.position)
        for child in self.children:
            print("\t", end="")
            child.show_details()


if __name__ == "__main__":
    print("Organização Hierárquica: ")
    general_manager = Management("Diretor Geral")
    manager_1 = Management("Gerente 1")
    manager_2 = Management("Gerente 2")
    dev_1 = Employee("Desenvolvedor 1")
    dev_2 = Employee("Desenvolvedor 2")
    dev_3 = Employee("Desenvolvedor 3")
    dev_4 = Employee("Desenvolvedor 4")
    manager_1.add(dev_1)
    manager_1.add(dev_2)
    manager_2.add(dev_3)
    manager_2.add(dev_4)

    general_manager.add(manager_1)
    general_manager.add(manager_2)
    general_manager.show_details()

