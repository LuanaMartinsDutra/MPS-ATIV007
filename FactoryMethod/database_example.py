from abc import ABC, abstractmethod

class DatabaseConnection(ABC):
    @abstractmethod
    def connect(self):
        pass

class MySQLConnection(DatabaseConnection):
    def connect(self):
        print("Conectado ao banco de dados MySQL...")

class PostgreSQLConnection(DatabaseConnection):
    def connect(self):
        print("Conectado ao banco de dados PostgreSQL...")
        
    

class ConnectionFactory(ABC):
    @abstractmethod
    def create_connection(self) -> DatabaseConnection:
        pass
    
    def get_name(self) -> str:
        pass

class MySQLConnectionFactory(ConnectionFactory):
    def create_connection(self) -> DatabaseConnection:
        return MySQLConnection()
    
    def get_name(self):
        return "MySQL"

class PostgreSQLConnectionFactory(ConnectionFactory):
    def create_connection(self) -> DatabaseConnection:
        return PostgreSQLConnection()

    def get_name(self):
        return "PostgreeSQL"
    
    
# class MongoDBConnection(DatabaseConnection):
#     def connect(self):
#         print("Conectado ao banco de dados MongoDB...")
        
        
# class MongoDBConnectionFactory(ConnectionFactory):
#     def create_connection(self) -> DatabaseConnection:
#         return MongoDBConnection()

#     def get_name(self):
#         return "MongoDB"

class SendMessageToDatabase:
    def __init__(self, factory: ConnectionFactory):
        self.factory = factory

    def connect_to_database(self):
        connection = self.factory.create_connection()
        connection.connect()
        
    def send(self):
        print(f"Enviando mensagem com {self.factory.get_name()}")


if __name__ == "__main__":
    mysql_factory = MySQLConnectionFactory()
    client = SendMessageToDatabase(mysql_factory)
    client.connect_to_database()
    client.send()
    
    print("----------------------------------")

    postgresql_factory = PostgreSQLConnectionFactory()
    client = SendMessageToDatabase(postgresql_factory)
    client.connect_to_database()
    client.send()
    
    print("----------------------------------")

    # mongo_factory = MongoDBConnectionFactory()
    # client = SendMessageToDatabase(mongo_factory)
    # client.connect_to_database()
    # client.send()
