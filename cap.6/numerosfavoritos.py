pessoas = {
    'miguel': ['17', '22'],
    'joao': ['10'],
    'tiago': ['11', '58'],
    'victor': ['29'],
    'ana': ['15', '343', '56', '97']
}
for nome, numeros in pessoas.items():
    if len(numeros) > 1:
        print(f'os numeros favoritos de {nome.title()} são: {numeros}')
    else:
        print(f'o numero favorito de {nome.title()} é: {numeros}')
