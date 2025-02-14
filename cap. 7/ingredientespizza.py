mensagem = 'insira um mensagem a pizza\n'
mensagem += 'caso queira encerrar o pedido digite "quit": '
ingrediente = ''
while ingrediente != 'quit':
    ingrediente = input(mensagem)
    if ingrediente != 'quit':
        print(f'adicionando: {ingrediente}')