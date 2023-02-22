class Request:
    def __init__(self, username: str, password: str, email: str):
        self.username = username
        self.password = password
        self.email = email

    def __str__(self) -> str:
        return '{' + f"username={self.username}, password={self.password}, email={self.email}" + '}'