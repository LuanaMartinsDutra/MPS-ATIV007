# Interface Segregation Principle - Gabriel Silva
from abc import ABC, abstractmethod


class InfoLogger(ABC):
    @abstractmethod
    def log_info(self, message: str) -> None:
        pass


class WarningLogger(ABC):
    @abstractmethod
    def log_warning(self, message: str) -> None:
        pass


class PaymentProcessor:
    def __init__(self, logger: InfoLogger) -> None:
        self.logger = logger

    def process_payment(self, amount: float) -> None:
        # process payment code here
        self.logger.log_info("Payment processed successfully")


class EmailSender:
    def __init__(self, logger: WarningLogger) -> None:
        self.logger = logger

    def send_email(self, recipient: str, message: str) -> None:
        # send email code here
        self.logger.log_warning("Email sent to {0}".format(recipient))
