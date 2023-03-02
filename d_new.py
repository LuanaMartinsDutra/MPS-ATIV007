# Dependency Inversion Principle - Gabriel Silva
from abc import ABC, abstractmethod


class IUser(ABC):
    @abstractmethod
    def get_email(self) -> str:
        pass

    @abstractmethod
    def get_phone(self) -> str:
        pass


class User(IUser):
    def __init__(self, email: str, phone: str) -> None:
        self.email = email
        self.phone = phone

    def get_email(self) -> str:
        return self.email

    def get_phone(self) -> str:
        return self.phone


class INotification(ABC):
    @abstractmethod
    def send_notification(self, user: IUser, message: str) -> None:
        pass


class EmailNotification(INotification):
    def send_notification(self, user: IUser, message: str) -> None:
        # send email code here
        pass


class SMSNotification(INotification):
    def send_notification(self, user: IUser, message: str) -> None:
        # send SMS code here
        pass
