# Integrantes:
# Tiago Farias Barbosa 2115310025
# Nickolas Javier Santos Livero 2115310042

from user_controller import UserController
from user_view import UserView
from user_model import UserDAO


def main():
    user_dao = UserDAO()
    user_view = UserView()
    user_controller = UserController(user_dao, user_view)

    user_controller.add_user()
    user_controller.show_users()


if __name__ == '__main__':
    main()
