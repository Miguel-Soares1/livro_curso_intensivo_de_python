respostas = {}
pesquisa_ativa = True

while pesquisa_ativa:
    nome = input('\nQual é o seu nome?: ')
    resposta = input('se pudesse visitar qualquer lugar do mundo, para qual lugar iria?: ')
    respostas[nome] = resposta
    add = input('adicionar mais uma pessoa? (digite sim ou nao): ')
if add == 'nao':
    pesquisa_ativa = False
for nome, resposta in respostas.items():
    print(f'o destino dos sonhos de {nome} seria {resposta}.')