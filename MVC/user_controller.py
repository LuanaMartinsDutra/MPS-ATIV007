from user_model import UserDAO
from user_view import UserView

class UserController:
    def __init__(self, user_dao: UserDAO, user_view: UserView):
        self.user_dao = user_dao
        self.user_view = user_view
    
    def add_user(self) -> None:
        name, email = self.user_view.get_user_data()
        self.user_dao.save_user(name, email)

    def show_users(self) -> None:
        users = self.user_dao.get_users()
        self.user_view.show_users(users)