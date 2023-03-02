Class OffState(State):
    
    def __init__(self, phone):
      super(OffState, self).__init(phone)
      
    def onHome(self):
      phone.setState(LockedState(phone))
      return phone.turnOn()
    
    def onOffOn(self):
      phone.serState(LockedState(phone))
      return phone.turnOn()
