from entities.request import Request
from handlers.email_handler import EmailHandler
from handlers.form_handler import FormHandler
from handlers.password_handler import PasswordHandler


class Form:
    def __init__(self, request: Request):
        self.request = request

    def is_valid_form(self) -> bool:
        # Instancia os handlers
        form_handler = FormHandler()
        email_handler = EmailHandler() 
        password_handler = PasswordHandler()

        # Configura a corrente de handlers
        form_handler.set_next(email_handler)
        email_handler.set_next(password_handler)

        return form_handler.handle(self.request)

def print_validation_message(is_valid: bool):
    print("Formulário válido" if is_valid else "Formulário inválido.")

def main():
    # Criando o formulário 
    form = Form(Request('gdsl', '1234', 'lima@gmail.com'))

    # Imprime se o formulário é válido ou não
    print_validation_message(form.is_valid_form())

main()