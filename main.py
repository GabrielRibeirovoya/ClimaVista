import Resquest.requestTime as requestTime
import os

def welcome(): 
    os.system('cls')
    print('Olá, seja bem-vindo ao serviços do ClimaVista!')
    input('Digite qualquer tecla para começarmos!')
    start_program()

def get_formatting_choice(formatting):

    options = {
        'C': 'Celsius',
        'F': 'Fahrenheit',
        'K': 'Kelvin'
    }

    if formatting in options:
        return options[formatting]
    else:
        print('Opção inválida. Por favor, escolha uma das opções válidas: C, F ou K.')
        input('Pressione qualquer tecla para tentar novamente.')
        start_program()

def start_program():
    os.system('cls')
    city = input('Insira a sua cidade: ')
    formatting = get_formatting_choice(input("Escolha o formato da temperatura (C, F, K): "))

    data = requestTime.request_city(city, formatting)
    

welcome()
    

