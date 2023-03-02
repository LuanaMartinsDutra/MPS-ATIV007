#MEDIATOR

class Mediator:
    def _init_(self):
        self.colleague1 = Colleague1(self)
        self.colleague2 = Colleague2(self)

    def send_message(self, message, colleague):
        if colleague == self.colleague1:
            self.colleague2.receive(message)
        else:
            self.colleague1.receive(message)


class Colleague1:
    def _init_(self, mediator):
        self.mediator = mediator

    def send(self, message):
        self.mediator.send_message(message, self)

    def receive(self, message):
        print(f"Colleague1 received: {message}")


class Colleague2:
    def _init_(self, mediator):
        self.mediator = mediator

    def send(self, message):
        self.mediator.send_message(message, self)

    def receive(self, message):
        print(f"Colleague2 received: {message}")


mediator = Mediator()

colleague1 = mediator.colleague1

colleague2 = mediator.colleague2

colleague1.send("Hello, colleague2!")
colleague2.send("Hi, colleague1!")