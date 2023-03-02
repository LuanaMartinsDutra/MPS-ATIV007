class Client:
    def __init__(self, client_type, communication):
        self.__type = client_type
        self.__communication = communication
        self.__connection = None
    
    def establish_connection(self, central_server):
        self.__connection = central_server
    
    def get_type(self):
        return self.__type
    
    def get_communication(self):
        return self.__communication
    
    def get_connection(self):
        return self.__connection
