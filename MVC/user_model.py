# Integrantes:
# Tiago Farias Barbosa 2115310025
# Nickolas Javier Santos Livero 2115310042

class User:
    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email


class UserDAO:
    def __init__(self):
        self.users = list()
    
    def save_user(self, name: str, email: str) -> None:
        new_user = User(name=name, email=email)
        self.users.append(new_user)
    
    def get_users(self) -> list[User]:
        return self.users