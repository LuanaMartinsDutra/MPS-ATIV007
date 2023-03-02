# Integrantes:
# Tiago Farias Barbosa 2115310025
# Nickolas Javier Santos Livero 2115310042

from user_model import User

class UserView:
    def __init__(self):
        pass

    def show_users(self, users: list[User]) -> None:
        print('Users')
        for user in users:
            print(f'name: {user.name} email: {user.email}')
    
    def get_user_data(self) -> tuple[str, str]:
        name = str(input('Name: '))
        email = str(input('Email: '))
        return name, email