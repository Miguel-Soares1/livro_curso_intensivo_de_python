#crie um programa que simule como os sites garantem que todos tenham um nome de usuario exclusivo
users = ['miguel', 'eric', 'tiago', 'felipe', 'ana']
new_users = ['TIAGO', 'pedro', 'Miguel']
for new_user in new_users:
    if new_user.lower() in users:
        print('esse nome de usuario ja esta sendo utilizado, tente outro nome.')
else:
    print('nome de usuario registrado com sucesso, bem vindo(a).')