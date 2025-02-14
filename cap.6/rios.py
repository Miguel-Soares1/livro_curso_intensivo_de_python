rios = {
    'nilo': 'egito',
    'amazonas':'brasil',
    'mississipi': 'eua'
}
for rio, pais in (rios.items()):
    print(f'o {rio.title()} esta localizado no pais {pais.title()}\n')

print('rios:')
for rio in sorted(rios.keys()):
    print(rio.title())

print('\n')

print('paises:')
for pais in rios.values():
    print(pais.title())
    