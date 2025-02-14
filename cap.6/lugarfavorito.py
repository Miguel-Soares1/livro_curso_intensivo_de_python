lugares = {'lugar 1': {
    'lugar': 'pisa',
    'nome': 'luis'
    },
    'lugar 2': {
    'lugar': 'paris',
    'nome': 'maria'
    },
    'lugar 3': {
    'lugar': 'londres',
    'nome': 'pedro'
    }           
}
for lugar, informacao in lugares.items():
    lugar = informacao['lugar']
    pessoa = informacao['nome']
    print(f'o lugar favorito de {pessoa.title()} é {lugar.title()}')