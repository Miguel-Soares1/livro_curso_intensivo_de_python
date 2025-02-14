from pathlib import Path
import json

def get_user_info(path):
    """função para coletar os dados do usuario e guarda-los em um dicionario."""
    user_info = {}
    user_info['name'] = input("qual é o seu primeiro nome? ")
    user_info['last name'] = input("qual é o seu ultimo nome? ")
    user_info['city'] = input("que cidade voce mora? ")

    with open(path, 'w') as file:
        json.dump(user_info, file)

    return user_info

def get_stored_user_info(path):
    """retorna os dados do usuario"""
    if Path(path).is_file():
        with open(path, 'r') as file:
            user_info = json.load(file)
        return user_info
    else:
        return None

def greet_user():
    """cumprimenta o usuario, utilizando dos dados que a pessoa informou da ultima vez"""
    path = 'remember_me.json'
    user_info = get_stored_user_info(path)
    nome_teste = input("qual é o seu nome?")
    """essa parte é o exercicio 10.14 (verificando usuario), caso quiser o ex 10.13, remova o input acima e o if abaixo"""
    if nome_teste != user_info['name']:
        print('esse nome é desconhecido por nós, por favor, informe os seus dados para criarmos um novo usuario.')
        user_info = get_user_info(path)
    if user_info:
        print(f"bem vindo de volta, {user_info['name']} {user_info['last name']}! como esta o clima em {user_info['city']}?" )
    else:
        user_info = get_user_info(path)
        print(f"nos vamos nos lembrar dessas informações da proxima vez!")

greet_user()