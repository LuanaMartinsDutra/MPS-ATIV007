from entities.request import Request
from handlers.email_handler import EmailHandler
from handlers.form_handler import FormHandler
from handlers.password_handler import PasswordHandler


def is_valid_form(request: Request) -> bool:
    form_handler = FormHandler()
    email_handler = EmailHandler() 
    password_handler = PasswordHandler()

    form_handler.set_next(email_handler)
    email_handler.set_next(password_handler)

    return form_handler.handle(request)

def print_validation_message(is_valid: bool, request: Request):
    print(request)
    print("Formulário válido" if is_valid else "Formulário inválido.")

def main():
    form_data_1 = Request('gdsl', '1234', 'lima@gmail.com')
    form_data_2 = Request('gdsl', '1234abc', 'lima@gmail.com')
    form_data_3 = Request('', '1234abc', 'lima@gmail.com')

    print_validation_message(is_valid_form(form_data_1), form_data_1)
    print_validation_message(is_valid_form(form_data_2), form_data_2)
    print_validation_message(is_valid_form(form_data_3), form_data_3)

main()