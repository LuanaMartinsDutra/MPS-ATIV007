class LockedState(State):
    def __init__(self, phone):
        super(LockedState, self).__init__(phone)

    def onHome(self):
        phone.setState(ReadyState(phone))
        return phone.unlock()

    def onOffOn(self):
        phone.setState(OffState(phone))
        return phone.lock()
