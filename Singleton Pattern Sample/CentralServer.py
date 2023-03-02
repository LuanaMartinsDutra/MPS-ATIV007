import threading

class CentralServer:
    __instance = None
    __lock = threading.Lock()  # Thread lock
    
    def __init__(self):
        if CentralServer.__instance is not None:
            raise Exception("You cannot get it in multiple instances, because it is a Singleton Class")
    
    @staticmethod
    def get_central_server():
        if CentralServer.__instance is None:
            with CentralServer.__lock:  # Acquire the lock before creating an instance
                if CentralServer.__instance is None:
                    CentralServer.__instance = CentralServer()
        return CentralServer.__instance
