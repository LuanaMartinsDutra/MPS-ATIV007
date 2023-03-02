# Dependency Inversion Principle - Gabriel Silva
class User:
    def __init__(self, email: str, phone: str) -> None:
        self.email = email
        self.phone = phone


class EmailNotification:
    def send_email(self, user: User, message: str) -> None:
        # send email code here
        pass


class SMSNotification:
    def send_sms(self, user: User, message: str) -> None:
        # send SMS code here
        pass
