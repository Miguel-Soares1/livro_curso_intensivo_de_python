pets = {
    'pet 1': {
        'tipo': 'cachorro',
        'nome': 'rex',
        'dono': 'miguel'
    },
    'pet 2': {
        'tipo': 'gato',
        'nome': 'felix',
        'dono': 'joao'
    },
    'pet 3': {
        'tipo': 'iguana',
        'nome': 'açafrão',
        'dono': 'pedro'
    }
}
for pet, informacao in pets.items():
    print(f'\n{pet.title()}')
    especie = informacao['tipo']
    nome_pet = informacao['nome']
    dono = informacao['dono']
    print(f'especie: {especie.title()}')
    print(f'nome do pet: {nome_pet.title()}')
    print(f'dono do pet: {dono.title()}')