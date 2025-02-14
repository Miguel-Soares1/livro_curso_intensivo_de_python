from pathlib import Path
lista_de_convidados = [] #criando uma lista de convidados
while len(lista_de_convidados) < 5: #caso a lista tenha menos de 5 convidados, o loop continua
    nome = input('digite o nome do convidado: ')
    lista_de_convidados.append(nome) # adicionando o nome do convidado a lista
    path = Path('livrodeconvidados.txt')
    path.write_text('\n'.join(lista_de_convidados)) # adicionando os nomes em linhas novas no arquivo

print('lista cheia!')