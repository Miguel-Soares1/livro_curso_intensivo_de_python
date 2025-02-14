pessoas = { 
    'pessoa 1': {
        'primeiro nome': 'miguel',
        'ultimo nome': 'dos santos',
        'idade': '19',
        'cidade': 'teresopolis'
    },
    'pessoa 2':{
        'primeiro nome': 'joao',
        'ultimo nome': 'santos',
        'idade': '20',
        'cidade': 'teresopolis'
    },
    'pessoa 3': {
        'primeiro nome': 'lucas',
        'ultimo nome': 'silva',
        'idade': '16',
        'cidade': 'teresopolis'
    }
}
for pessoa, informacao in pessoas.items():
    print(f'\n{pessoa.title()}')
    primeiro_nome = informacao['primeiro nome']
    ultimo_nome = informacao['ultimo nome']
    idade = informacao['idade']
    cidade = informacao['cidade']
    print(f'primeiro nome: {primeiro_nome.title()}')
    print(f'ultimo nome: {ultimo_nome.title()}')
    print(f'idade: {idade}')
    print(f'cidade: {cidade.title()}')