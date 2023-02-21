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

class MySQLConnectionFactory(ConnectionFactory):
    def create_connection(self) -> DatabaseConnection:
        return MySQLConnection()

class PostgreSQLConnectionFactory(ConnectionFactory):
    def create_connection(self) -> DatabaseConnection:
        return PostgreSQLConnection()

class DatabaseClient:
    def __init__(self, factory: ConnectionFactory):
        self.factory = factory

    def connect_to_database(self):
        connection = self.factory.create_connection()
        connection.connect()



mysql_factory = MySQLConnectionFactory()
client = DatabaseClient(mysql_factory)
client.connect_to_database()

postgresql_factory = PostgreSQLConnectionFactory()
client = DatabaseClient(postgresql_factory)
client.connect_to_database()
