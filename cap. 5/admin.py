#crie uma lista com 5 nomes de usuarios. se o nome do usuario for admin, exiba uma mensagem especial, caso contrario,
#exiba uma mensagem generica
users = ['miguel', 'admin', 'joao', 'matheus', 'julia']
for user in users:
    if user == 'admin':
        print('ola administrador(a), gostaria de ver um relatorio de status?')
else:
    print(f'olá {user} bem vindo(a) de volta')