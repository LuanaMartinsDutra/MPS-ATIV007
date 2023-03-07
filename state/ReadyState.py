class ReadyState(State):
     def __init__(self, phone ):
            super(ReadyState, self).__init__(phone)

     def onHome(self):
        return phone.home()

     def onOffOn(self):
        phone.setState(OffState(phone))
        return phone.lock()
