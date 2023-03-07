
class Phone(object):
    state = State()
    def __init__(self):
        self.state = OffState(self)

    def setState(self, state):
        self.state = state

    def lock (self):
        return "Locking phone and turning off the screen"
    def home(self):
        return "Going to home-screen"

    def unlock(self):
        return "Unlocking the phone to home"
    def turnOn(self):
        return "Turning screen on "
    def clickHome(self):
        return self.state.onHome()
    def clickPower(self):
        return self.state.onOff()
