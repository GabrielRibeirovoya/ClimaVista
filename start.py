import RequestTime.requestTime as requestTime
import os
import json
import unicodedata
import subprocess

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

    print(f'A temperatura na cidade {data['city']} esta em torno de {data['temp']}.')

    data.clear()

    sender_today = input('Deseja receber e-mail todos os dias referente a o clima (S/n): ')
    
    if sender_today == 'S':
        temperature_shipping()
    else:
        end_program()


def temperature_shipping():
    os.system('cls')

    city = input('Insira a cidade que ira ser monitorada: ')
    city = unicodedata.normalize('NFKD', city).encode('ASCII', 'ignore').decode('ASCII')
    formatting = get_formatting_choice(input("Escolha o formato da temperatura (C, F, K): "))
    name = input('Insira seu nome: ')
    name = unicodedata.normalize('NFKD', name).encode('ASCII', 'ignore').decode('ASCII')
    email = input('Insira seu endereço de e-mail: ')
    time_sender = input('Qual horário deseja receber o e-mail (Hh:Mm): ')

    data = {'email': email,
            'nome': name,
            'city': city,
            'formatting': formatting,
            'StartTime': time_sender.replace(':', ''),
            'frequency': 'Daily',
            'frguments': '--example-arg value',
            'ai': 'inativo'}
    
    json_str = json.dumps(data)

    with open('sender.json', 'w') as arquivo:
        arquivo.write(json_str)

    start_powershell()
    os.system('cls') 

def end_program():
    os.system('cls')

def start_powershell():
    current_dir = os.path.dirname(os.path.abspath(__file__))

    powershell_script = os.path.join(current_dir, "script.ps1")

    try:
        result = subprocess.run(
            ["powershell.exe", "-ExecutionPolicy", "Bypass", "-File", powershell_script],
            capture_output=True, text=True, check=True
        )

        print("Saída do PowerShell:")
        print(result.stdout)

        if result.stderr:
            print("Erros do PowerShell:")
            print(result.stderr)

    except subprocess.CalledProcessError as e:
        print(f"Erro ao executar o script PowerShell: {e}")
        print(f"Saída do erro: {e.stderr}")

def colectorTime(city, formatting):
    return requestTime.request_city(city, formatting)

welcome()
    

