# Program to check input
# type in Python
from apps.validators import Validators
import sys


def menu():
    print("###### Validadores #######")
    print("""
        1 - Identificador
        2 - Email
        3 - Password
        4 - Idade para trabalho
        5 - Encerrar o programa
        """)


def app():
    while True:
        menu()
        option = int(input('Informe sua opção: '))
        if option == 0:
            continue
        elif option == 1:
            view_identifier()
        elif option == 2:
            view_email()
        elif option == 3:
            view_password()
        elif option == 4:
            view_age_to_work()
        elif option == 5:
            break
        else:
            print("Opção inválida. Tente novamente com: ")
            menu()


def view_identifier():
    identified = input("Entre com um identificador: ")
    validators.check_valid_identifier(identified)


def view_email():
    email = input("Entre com um email: ")
    validators.check_email(email)


def view_password():
    password = input("Entre com um password: ")
    validators.check_password(password)


def view_age_to_work():
    age = int(input("Entre com uma idade: "))
    validators.check_age_for_work(age)


if __name__ == "__main__":
    validators = Validators()
    app()
