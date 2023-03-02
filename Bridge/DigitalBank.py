# Aluno: Julio Cesar Ferreira de Souza

from abc import ABC, abstractmethod

class PaymentAbstraction(ABC):
    @abstractmethod
    def authorize(self):
        pass

    @abstractmethod
    def check_balance(self):
        pass


class CreditCardPayment(PaymentAbstraction):
    def authorize(self):
        print("Authorizing credit card payment...")

    def check_balance(self):
        print("Checking credit card balance...")


class PaypalAbstraction(PaymentAbstraction):
    def authorize(self):
        print("Authorizing Paypal payment...")

    def check_balance(self):
        print("Checking Paypal balance...")


class PaymentImplementation:
    def __init__(self, abstraction: PaymentAbstraction):
        self._abstraction = abstraction

    def authorize(self):
        self._abstraction.authorize()

    def check_balance(self):
        self._abstraction.check_balance()

    def capture_payment(self):
        print("Capturing payment...")
        self._abstraction.authorize()
        self._abstraction.check_balance()
        print("Payment captured.")


class CreditCardProcessor(PaymentImplementation):
    def __init__(self):
        super().__init__(CreditCardPayment())


class PaypalProcessor(PaymentImplementation):
    def __init__(self):
        super().__init__(PaypalAbstraction())


# Exemplo de uso
if __name__ == "__main__":
    # Cria um processador de pagamento via cartão de crédito
    credit_card_processor = CreditCardProcessor()
    
    # Autoriza o pagamento via cartão de crédito
    credit_card_processor.authorize()
    
    # Verifica o saldo do cartão de crédito
    credit_card_processor.check_balance()
    
    # Captura o pagamento
    credit_card_processor.capture_payment()

    print("")
    
    # Cria um processador de pagamento via Paypal
    paypal_processor = PaypalProcessor()
    
    # Autoriza o pagamento via Paypal
    paypal_processor.authorize()
    
    # Verifica o saldo do Paypal
    paypal_processor.check_balance()
    
    # Captura o pagamento
    paypal_processor.capture_payment()